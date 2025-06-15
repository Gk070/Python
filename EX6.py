# Excercise 6 - Hypotnuese of a right triangle

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

hypotnuese = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"Hypotnuese is: {hypotnuese}cm")