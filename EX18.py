# Rock Paper Scissor game

import random

option = ("rock", "paper", "scissor")

round = int(input("Enter the no:of rounds you want to play: "))

point = 0

for i in range(round):
    print()
    player = input("Enter (Rock, paper or scissor): ").lower()
    computer = random.choice(option)

    while player not in option:
        player = input("Enter (Rock, paper or scissor): ").lower()

    if ((player == "paper" and computer == "rock") or (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper")):
        point += 1
        print()
        print(f"Computer: {computer}")
        print("Player Wins")

    elif player == computer:
        point += 0.5
        print()
        print(f"Computer: {computer}")
        print("It's a tie")
    else:
        print()
        print(f"Computer: {computer}")
        print("Computer wins")

print()
print(f"Final score is: {point}/ {round}")