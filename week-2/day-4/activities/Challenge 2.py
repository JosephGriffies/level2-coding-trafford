pin = 1234
pin2 = input("What is your PIN")
pin2 = int(pin2)
balance = 10000
withdrawal = input("How much money would you like to withdraw")
withdrawal = int(withdrawal)

if pin2 == pin and balance >= withdrawal:
    print("Dispensing Cash")
    balance -= withdrawal
    print(f"Your new balance is {balance}")
else:
    print("Trasaction Invalid")