import random

x = 0

for y in range(6):
    x = (random.randint(1,30))
    if x % 7 == 0:
        print(f"The number {x} is divisible by 7")
    else:
        print(f"The number {x} is not divisible by 7")