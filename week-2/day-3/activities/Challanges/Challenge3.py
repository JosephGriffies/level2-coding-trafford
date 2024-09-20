num = input("What is your number")
try:
    num = int(num)#checks if num is an integer and makes num considered an integer value
except ValueError:
    print("This is not an integer. Please enter a valid integer.")
    exit()
value1 = num
value1 %= 3
value2 = num
value2 %= 7

if value1 == 0 and value2 == 0:
    print("Fizz bang")
elif value1 == 0 and value2 != 0:
    print("Fizz")
elif value1 != 0 and value2 == 0:
    print("bang")
else:
    print(num)