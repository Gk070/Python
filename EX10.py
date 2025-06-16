# Validate User Input Excercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("Username cannot be more than 12 characters")
elif username.find(" ") != -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain numbers")
else:
    print(f"Welcome {username}!")