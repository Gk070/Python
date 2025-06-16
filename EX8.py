# Weight Converter

weight = float(input("Enter weight: "))
unit = input("Enter unit(K-Kilograms L-pounds): ")

if unit == "K":
    print(f"Weight in Pounds is: {round(weight * 2.20462, 2)}lbs")
elif unit == "L":
    print(f"Weight in Kilogram is: {round(weight / 2.20462, 2)}kg")
else:
    print("Invalid operator")