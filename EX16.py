# Concession Stand Program

menu = {"popcorn": 100,
        "nachos": 150,
        "hot dogs": 120,
        "puffs": 100,
        "wraps": 120}

print("--------MENU--------")
for key, value in menu.items():
    print(f"| {key:10}: ₹{value} |")
print("--------------------")
print()

cart = []

while True:
    food = input("Enter the food item (q to quit): ").lower()
    if(food == 'q'):
        break
    if menu.get(food) is not None:
        cart.append(food)
    
total = 0
print()
print("Ordered items")
print("-------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print()

print(f"Total amount is: ₹{total}")