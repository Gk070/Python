# Temprature Conversion Program

temprature = float(input("Enter temprature: "))
unit = input("Enter unit(C-Celsius F-Farenheit): ")

if unit == "C":
    print(f"Temprature in farenheit is: {round((temprature * (9.0 / 5)) + 32, 2)}f")
elif unit == "F":
    print(f"Temprature in Celsius is: {round((temprature - 32) * (5.0 / 9), 2)}f")    
else:
    print("Invalid Unit")