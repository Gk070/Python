# Hangman Game

from wordsList import words
import random

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "   "),
    6: (" O ",
        "/|\\",
        "/  "),
    7: (" O ",
        "/|\\",
        "/ \\")
}

def displayHangman(wrong_guess):
    print("\n**********")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("**********")

def main():
    print("***************************")
    print("* Welcome to Hangman Game *")
    print("***************************")
    wrong_guess = 0
    answer = random.choice(words)
    guessed = ""

    hint = ["_"] * len(answer)

    while True:
        displayHangman(wrong_guess)
        guess = input("Enter guess: ")
        if len(guess) > 1 and not guess.isalpha():
            print("Invalid Guess")
        else:
            if guess in guessed:
                print("Already guessed")
                continue
            elif guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guess += 1

        if wrong_guess >= 7:
            displayHangman(wrong_guess)
            print(f"The Animal was: {answer}")
            print("You Lost!")
            break
        elif "_" not in hint:
            print("Hurray! You won")
            break
        
        
        guessed += guess
        print("\n" + " ".join(hint))

if __name__ == "__main__":
    main()