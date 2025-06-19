# Number Guessing Game

import random

lowest_num = 1
highest_num = 100
ans = random.randint(lowest_num, highest_num)

guesses = 1
while True:
    guess = int(input(f"Enter a number between {lowest_num} and {highest_num}: "))
    if guess > highest_num or guess < lowest_num:
        print("Guess out of range!")
        print("Enter a number between {lowest_num} and {highest_num}")

    elif guess != ans:
        if guess > ans:
            print("\nGuessed number is larger than the actual number")
            guesses += 1
        
        else:
            print("\nGuessed number is smaller than the actual number")
            guesses += 1

    else:
        print("\nYour guess is correct")
        print(f"No:of guess are {guesses}")
        break