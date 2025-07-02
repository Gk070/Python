# Banking Program 

def deposit():
    
    amount = int(input("\n💰 Enter amount to be deposited: ₹"))

    if amount < 0:
        print("💵 Amount cannot be less than ₹0 💵")
        return 0
        
    return amount

def showBalance():
    print(f"Your account balance is: ₹{balance} 💰")

def withdraw():
    
    amount = int(input("\n💰 Enter amount to withdraw: ₹"))

    if amount > balance:
        print(f"💵 Amount cannot be greater than balance ₹{balance} 💵")
        return 0
        
    return amount

balance = 0

while True:

    print()
    print("**************************")
    print("* 🏦 Banking Program 🏦 *")
    print("**************************")
    print("  1. Deposit")
    print("  2. Balance")
    print("  3. Withdraw")
    print("  4. Exit")
    print("**************************")
    print()

    choice = int(input("Enter Choice: "))

    if choice == 1:
        balance += deposit()

    elif choice == 2:
        showBalance()

    elif choice == 3:
        balance -= withdraw()

    elif choice == 4:
        print("\nHave a nice day!")
        break

    else:
        print("Invalid Option")