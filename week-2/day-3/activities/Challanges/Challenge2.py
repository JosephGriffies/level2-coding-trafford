num = input("What is your number")
try:
    num = int(num)
except ValueError:
    print("This is not an integer. Please enter a valid integer.")
    exit()
value1 = num
value1 %= 3
value2 = num
value2 %= 5

if value1 == 0 and value2 == 0:
    print("This number is divisible by 3 and 5")
elif value1 == 0 and value2 != 0:
    print("This number is divisible by 3")
elif value1 != 0 and value2 == 0:
    print("This number is divisible by 5")
else:
    print("The number is not divisible by 3 or 5")
