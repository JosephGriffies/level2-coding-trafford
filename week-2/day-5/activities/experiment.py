choice = 0
well = 0

while choice >= 0:
    print("You find yourself in a funny town")
    if well == 0:
        travel = input("What would you like to do in the town? (1)Talk to people, (2)See what you can find at the shop (3) Check out the garden")
        travel = int(travel)
    else:
        travel = input("What would you like to do in the town? (1)Talk to people, (2)See what you can find at the shop (3) Check out the garden (4) Investigate the well")
        travel = int(travel)
    if travel == 1:
        print("You see a person looking around the well for something")
        print("Hey there traveler, what can I do to help you?")
        choice = input("(1)ask about any rumours, (2) ask if anything is wrong")
        choice = int(choice)
        if choice == 1:
            print("Well is odd")
            well = 1
        elif choice == 2: 
            print("The king is mean.")
        else:
            print("I didn't quite catch that")