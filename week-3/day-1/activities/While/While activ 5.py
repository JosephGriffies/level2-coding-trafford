z = 0

for x in range (1,21):
    for y in range(1,21):
        if x % y != 0:
            z += 1
    if z >= 18 and x != 1:
        print(f"{x} is a prime number")
    z = 0
