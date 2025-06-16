# A simple python calculator

operator = input("Enter operator(+ - * /): ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if operator == "+":
    print(f"Sum is: {round(num1 + num2, 2)}")
elif operator == "-":
    print(f"Difference is: {round(num1 - num2, 2)}")
elif operator == "*":
    print(f"Product is: {round(num1 * num2, 2)}")
elif operator == "/":
    print(f"Divisor is: {round(num1 / num2, 2)}")
else:
    print("Invalid operator")