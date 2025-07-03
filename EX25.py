# Python Slot Machine

import random

def spinRow():
    symbols = ['🍒', '🍉', '🥭', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def display(results):
    print()
    print(" | ".join(results))

def pay(results, bet):
    if results[0] == results[1] == results[2]:
        
        print("💸You Won💸")

        if results[0] == '🍒':
            return bet * 3
        if results[0] == '🍉':
            return bet * 4
        if results[0] == '🥭':
            return bet * 5
        if results[0] == '🔔':
            return bet * 10
        if results[0] == '⭐':
            return bet * 20
        
    else:
        print("🤗Better luck next time🤗")
        return 0

def main():

    print()
    print("**************************")
    print(" Welcome to Python Slots  ")
    print("**************************")
    print("Symbols: 🍒 🍉 🥭 🔔 ⭐")
    print("**************************")

    balance = float(input("\nEnter amount to deposit: ₹"))

    while balance > 0:
        print(f"\n💰 Current balance: ₹{balance}")

        bet = float(input("💵 Enter bet amount: ₹"))

        if bet > balance:
            print("\n💸Insufficient Funds💸")
            op = input("💸 Do you want to add fund(Y/N): ").upper()
            if op == 'Y':
                payment = float(input("💸Enter amount to deposit: ₹"))

            balance += payment
        else:
            balance -= bet
            results = spinRow()
            display(results)
            balance += pay(results, bet)

            ex = input("\n💸 Do you want to bet again(Y/N): ").upper()
            if ex == "N":
                break

if __name__ == "__main__":
    main()