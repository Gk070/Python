# Arbitary Arguments

def func(*args, **kwargs):
    for arg in args:
        print(arg, end="  ")
    print()
    for value in kwargs.values():
        print(value, end="  ")

func("Mr.", "Harikrishnan", address="Lekshmi Vihar", place="Adoor", city="Adoor", state="Pathanamthitta", country="India")