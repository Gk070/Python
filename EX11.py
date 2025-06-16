# Compount Interest Calculator

P = int(input("Enter the principle amount: "))
r = float(input("Enter the annual interest rate: "))
t = float(input("Enter for how many years the money is invested: "))

print(f"Compound interest is: ₹{(P * pow((1 + (r / 100)), t))}")