# Dice 

import random

dice = {1: ("------------",
             "|          |",
             "|     ●    |",
             "|          |",
             "------------",),
        2: ("------------",
            "| ●        |",
            "|          |",
            "|        ● |",
            "------------",),
        3: ("------------",
            "| ●        |",
            "|     ●    |",
            "|        ● |",
            "------------",),
        4: ("------------",
            "|  ●    ●  |",
            "|          |",
            "|  ●    ●  |",
            "------------",),
        5: ("------------",
            "|  ●     ● |",
            "|     ●    |",
            "|  ●     ● |",
            "------------",),
        6: ("------------",
            "|  ●    ●  |",
            "|  ●    ●  |",
            "|  ●    ●  |",
            "------------",)}

rolls = []

n = int(input("Enter no:of times the dice to be rolled: "))

for i in range(n):
    die = random.randint(1, 6)
    rolls.append(die)

for roll in range(n):
    for die in dice.get(rolls[roll]):
        print(die)
    print()