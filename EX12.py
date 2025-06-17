# Count Down Timer Program

import time

t = int(input("Enter the time in seconds: "))

for i in range(t, 0, -1):
    sec = i % 60
    min = int(i / 60) % 60
    hr = int(i / 3600) % 24
    day = int(i / 86400)
    print(f"{day:02}:{hr:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("Time's Up") 