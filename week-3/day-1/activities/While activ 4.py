num = 1
while num != 0: 
    num = input("Please provide an integer that is 1 or above unless you want to close the program in which case type 0.")
    num = int(num)
    if num != 0:
        for x in range(1,13):
            value = num*x
            print(value)