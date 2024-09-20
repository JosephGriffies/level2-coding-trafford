num1 = input("What is your first number")
try:
    num1 = int(num1)#checks if num is an integer and makes num considered an integer value
except ValueError:
    print("This is not an integer. Please enter a valid integer.")
    exit()
num2 = input("What is your second number")
try:
    num2 = int(num2)#checks if num is an integer and makes num considered an integer value
except ValueError:
    print("This is not an integer. Please enter a valid integer.")
    exit()
num3 = num1 + num2
num3 %= 2
if num3 == 1:
    print("The results are odd")
else:
    print("The results are even")