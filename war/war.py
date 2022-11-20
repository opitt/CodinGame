import sys
from collections import deque


def getinput():
    with open("pat.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        yield line.strip()


I = getinput()


def input():
    return next(I)


v = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}
n = int(input())  # the number of cards for player 1
p1 = deque([v[input()[:-1]] for _ in range(n)])  # the n cards of player 1

n = int(input())  # the number of cards for player 2
p2 = deque([v[input()[:-1]] for _ in range(n)])  # the n cards of player 2


print(" ".join([f"{c: >2}" for c in p1]))
print(" ".join([f"{c: >2}" for c in p2]))


def p(*m):
    print(m, file=sys.stderr, flush=True)

rounds = 1
pot1, pot2 = [], []
while len(p2) > 0 and len(p1)>0:
    c1 = p1.popleft()
    c2 = p2.popleft()
    pot1.append(c1)
    pot2.append(c2)

    if c1 > c2:
        p1.extend(pot1)
        p1.extend(pot2)
        pot1, pot2 = [],[]
        rounds += 1
    elif c1<c2:
        p2.extend(pot1)
        p2.extend(pot2)
        pot1, pot2 = [],[]
        rounds += 1
    else:
        # WAR
        if len(p1)<3 or len(p2)<3:
            break
        pot1.extend([p1.popleft() for _ in range(3)])
        pot2.extend([p2.popleft() for _ in range(3)])


if len(p1) == 0:
    print(f"2 {rounds}")
elif len(p2) == 0:
    print(f"1 {rounds}")
else:
    print(f"PAT")
