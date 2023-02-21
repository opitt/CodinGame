# https://www.codingame.com/ide/puzzle/breaking-apart

# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import sys
import re


def is_vovel(c):
    return c.lower() in "aeiou"


def split_word(w, space):
    p1, p2 = "", ""
    syls = word2syl_reg(w)
    if len(syls[0]) == 1:
        syls[1] = syls[0]+syls[1]
        syls = syls[1:]
    for i, s in enumerate(syls):
        if len(p1+s) <= space:
            p1 += s
        else:
            p2 = "".join(syls[i:])
            break
    return p1, p2


def word2syl(w):
    # solution without regular expression
    syls = []
    syl = ""
    vov_found = False
    for a, b in zip(w[:-1], w[1:]):
        if not vov_found:
            syl += a
            vov_found = is_vovel(a)
        else:
            if is_vovel(a):
                syls.append(syl)
                syl = a
                vov_found = True
            else:
                if is_vovel(b):
                    syls.append(syl)
                    syl = a  # not in "aeoiu"
                    vov_found = False
                else:
                    syl += a
                    syls.append(syl)
                    syl = ""
                    vov_found = False
    if not vov_found:
        syl += b
    else:
        if is_vovel(b):
            syls.append(syl)
            syl = b
        else:
            syl += b
    syls.append(syl)
    return syls


def word2syl_reg(w):
    # split the given word in sylables using regex
    # (revers the word to find the sticky consonants with their vovel)
    regex = r"[^aeiou][aeiou][^aeiou]|[^aeiou][aeiou]|[aeiou][^aeiou]|[aeiou]"
    syls = [s[::-1] for s in re.findall(regex, w[::-1], re.IGNORECASE)[::-1]]
    return syls

def solve(length, words):
    word, lines = "", [""]
    while words or word:
        # take the word, if word is fully used
        if word == "":
            word, *words = words
        empty = len(lines[-1]) == 0
        space = length - len(lines[-1])
        # if word fits into current line, use it
        if space >= len(word) + (0 if empty else 1):
            lines[-1] += ("" if empty else " ") + word
            word = ""
        else:
            # split the word
            space -= 1  # need to save space for "-"
            # need to save space for " ", if there are already words in the line
            space -= 0 if empty else 1
            part1, part2 = split_word(word, space)
            if part1:
                lines[-1] += f"{part1}-" if empty else f" {part1}-"
                word = part2
                # the remaining word goes on the next line:
                lines.append("")
            else:
                # word cant be broken to fit in this line. try next line.
                lines.append("")
    return lines

if __name__ == "__main__":
    length = int(input("Length:"))
    words = input("Words:")
    lines = solve(length, words.split())
    print(*lines, sep="\n")
