#if else

password = input("What is your password?")

length = len(password)

if length <= 7:
    print("Your password is too short. Please make it at least 8 characters long.")
else:
    print("Your password is long enough.")