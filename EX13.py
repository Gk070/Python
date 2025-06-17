# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter name of the food to be purchased (q to Quit): ")
    if food.lower() == "q":
        break
    foods.append(food)
    price = float(input(f"Enter the price of the {food}: ₹"))
    prices.append(price)

print("----- 🛒 Your Cart 🛒 -----")
print()

i = 1
for food in foods:
    print(f"Item {i}: {food}")
    i += 1

for price in prices:
    total += price

print()
print(f"Total amount is: ₹{total}")