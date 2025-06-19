# Default arguments

import time

def count(end, start = 0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)

count(10)
print("Done!")