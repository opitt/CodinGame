# https://www.codingame.com/ide/puzzle/breaking-apart

# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# import sys
import re

def is_vovel(c):
    return c.lower() in "aeiou"

def split_word(w, space):
    space -= 2  # " " and -
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
    # (revers the word to find the sticky consonunts with their vovel)
    regex = r"[^aeiou][aeiou][^aeiou]|[^aeiou][aeiou]|[aeiou][^aeiou]|[aeiou]"
    syls = [s[::-1] for s in re.findall(regex, w[::-1])[::-1]]
    return syls


#length = int(input())
length = 63
#words = input().split()
words = "Sed ut perpiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi arcitecto beatae vitae dicta sun expicabo Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciut Neque porro quisquam et qui dolorem ipsum quia dolor sit amet consectetur adipisci velit sed quia non numquam eius modi tempora incidun ut".split()
words = "Dertana et alioumatok gorigo te".split()
for w in words:
    print(w, word2syl(w))
    print(w, word2syl_reg(w))

word = ""
lines = [""]
while words or word:
    # take the word, if word is fully used
    if word == "":
        word, *words = words
    # if word fits into current line, use it
    if length - len(lines[-1]) >= len(word) + 1:
        lines[-1] = (lines[-1] + f" {word}").lstrip()
        word = ""
    else:
        # split the word
        part1, part2 = split_word(word, length - len(lines[-1]))
        if part1:
            lines[-1] = f"{lines[-1]} {part1}-".lstrip()
            lines.append("")
            word = part2
        else:
            # try next line
            lines.append("")

print(*lines, sep="\n")
