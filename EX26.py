# Encrypt message

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

org_msg = input("\nEnter a message to be encrypted: ")
encrypt = ""

for char in org_msg:
    index = chars.index(char)
    encrypt += keys[index]

print(f"Encrypted message is: {encrypt}\n")