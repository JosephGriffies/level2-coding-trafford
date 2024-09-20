time = input("What time is it")
home = input("What town is your home in")
work = input("What place do you work at")
time = int(time)

if time <= 7:
    print(f"I am at my home in {home}")
elif time >= 18:
    print (f"I am at my home in {home}")
elif time == 8:
    print(f"I am commuting to {work}")
elif time == 17:
    print(f"I am commuting to {home} from {work}")
else:
    print(f"I am at {work}")