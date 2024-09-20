#If else + input

age = input("How old are you?")
country = input("Where are you from")

if age >="18"and country == "UK":
    print ("Yes, I can serve you")
elif age >="18"and country != "UK":
    print ("I cam only serve you if you are legally considered an adult in your country")
else:
    print ("I'm sorry I can not serve you")