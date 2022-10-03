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


# hopefully my comments below will help some people. (Also I want to add that for C# users this code is running in old .net 4 version.)
# How to get cards of both players in proper order after one of the player’s win:
# if player N wins the battle, cards are added to the bottom of his deck in this order:
# 1st player’s card he used to battle
# 1st player’s three war cards
# 1st player’s card used to win the war through battle (or if not resolved it is still added and new war starts)
# 1st player’s next three war cards if previous battle card didn’t resolve the war and new war started
# … and so on until all war and battle cards of player 1 are retrieved and put at the bottom of player’s N deck
# then …
# 2nd player’s card he used to battle
# … and so one and as above but for 2nd player
# PAT happens if:
# if any player runs out of cards but battle is in progress (if war is in progress it means that battle is in progress too)
# battle is in progress if battle cards are out but winner cannot be determined as there are not enough cards on both sides to go to war
# ROUNDS increase:
# round only increase when battle is won/resolved (war is not won without battle being won/resolved first)
# in complex case you can get:
# unresolved battle (equal cards’ strength) which means war starts
# war (which means just additional 3 cards taken (if there are cards available, otherwise PAT)
# another unresolved battle
# another war
# resolved/won battle
# … above is counted not as 3 rounds but as one as only one battle was won/resolved

# You battle with 1st card from each deck, if they are the same, you start the war.
# For war you take next 3 cards and put them aside (don’t battle them), then you take 4th card and battle only that one.
# After that winner takes all (10 cards, 5 from P1, 5 from P2).

rounds = 0
war1, war2, pot = [], [], []
while True:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if len(p1) == 0 or len(p2) == 0:
        rounds += 1
        break
    if c1 > c2:
        pot.append(c1)
        pot.extend(war1)
        pot.append(c2)
        pot.extend(war2)
        p1.extend(pot)
        rounds += 1
        war1, war2, pot = [], [], []
    elif c1 < c2:
        pot.append(c1)
        pot.extend(war1)
        pot.append(c2)
        pot.extend(war2)
        p2.extend(pot)
        rounds += 1
        war1, war2, pot = [], [], []
    else:
        # WAR
        if len(p1) <= 3 or len(p2) <= 3:
            break
        war1.append(c1)
        war1.extend([p1.popleft() for _ in range(3)])
        war2.append(c2)
        war2.extend([p2.popleft() for _ in range(3)])

if len(p1) == 0:
    print(f"2 {rounds}")
elif len(p2) == 0:
    print(f"1 {rounds}")
else:
    print(f"PAT")
