import random
player =20 #Players hp
dragon = 30 #Dragons hp
turn_count = 1 #A way to track the turn count used for boss patterns and super attack
charge = 0 #The value the dragon uses to deal bonus damage every 3 turns
comeback = 0 #The value used to track when the superattack is ready and how much damage it will deal
cooldown = 0
critp = 100 
critd = 100 #above variables are established to prevent errors
print("Oh no a dragon has appeared")

while player <= 100: #loops everything below until the code is closed
    if player >= 1 and dragon >= 1: #checks to see if the player and dragon are alive
        print(f"It is turn {turn_count}")
        if comeback == 0 and cooldown <=4:
            move = input("Would you like to attack (1), heal (2), or defend (3)")
        else:
            move = input("YOU ARE POWERED UP! Would you like to attack (1), heal (2), defend (3) or use your super attack (4)")
        move = int(move) #sets the variable move as an integer to allow it to be used in if statements
        if move == 1:
            turn_count += 1 #adds 1 to the turn count to enable mechanics like the super attack and the dragons strong attack
            damagep = (random.randint(1,6)) #decides how much damage is dealt
            critp = (random.randint(1,100)) 
            if critp <= 10: #Chance for a critical hit
                damagep *= 2 #If a critical hit happens doubles damage
            dragon -= damagep #What actually deals damage
            if critp >=11:
                print(f"You dealt {damagep} damage to the dragon leaving it with {dragon} hp")
            else: 
                print(f"WOAH! A CRITICAL HIT. You dealt {damagep} damage to the dragon leaving it with {dragon} hp")
            if dragon>=1: #checks dragon is alive after attacking
                damaged = (random.randint(1,6))
                damaged += charge #every 3 turns the dragon deals bonus damage with the charge variable
                critd = (random.randint (1,100))
                if critd <= 5: #the dragons crit chance, lower than the player characters
                    damaged *= 2
                player -= damaged #how the player takes damage
                if critd >= 6:
                    print(f"The dragon attacks, you took {damaged} and you now have {player} hp")
                else:
                    print(f"WATCH OUT! The dragon landed a critical hit and dealt {damaged} damage to you leaving you with {player} hp")
        elif move == 2:
            turn_count += 1
            heal = (random.randint(3,9)) #decides how much hp to heal
            player += heal #how hp is healed
            if player >= 20:
                player =20 #fail safe to prevent healing over your max hp
            print (f"You healed yourself for {heal} and now you have {player}hp")
            if dragon>=1: #This check is not necessary 
                damaged = (random.randint(1,6))
                damaged += charge 
                critd = (random.randint (1,100))
                if critd <= 5:
                    damaged *= 2
                player -= damaged
                if critd >= 6:
                    print(f"The dragon attacks, you took {damaged} and you now have {player} hp")
                else:
                    print(f"WATCH OUT! The dragon landed a critical hit and dealt {damaged} damage to you leaving you with {player} hp")
        elif move == 3:
            turn_count += 1
            defend = (random.randint(1,6)) #decides how much to reduce damage by
            print(f"You raised your guard, the next attack will deal up to {defend} less damage")
            if dragon>=1: #This check here is uneccessary
                damaged = (random.randint(1,6))
                damaged += charge
                damaged -= defend
                if damaged <= 0: 
                    damaged = 1 #fail safe to prevent the dragon dealing 0 or less damage
                critd = (random.randint (1,100))
                if critd <= 5:
                    damaged *= 2
                player -= damaged
                if critd >= 6:
                    print(f"The dragon attacks, you took {damaged} and you now have {player} hp")
                else:
                    print(f"WATCH OUT! The dragon landed a critical hit and dealt {damaged} damage to you leaving you with {player} hp")
        elif move == 4 and comeback == 10 or cooldown == 5:
            turn_count += 1
            critp = (random.randint(1,100))
            if critp <= 5: #The comeback attack has a lower crit chance
                comeback *= 2
            dragon -= comeback
            comeback = 0 #Means comeback can only be used once
            cooldown = 0
            if critp >=6:
                print(f"You strike with all your power. You dealt 10 damage to the dragon leaving it with {dragon} hp")
            else: 
                print(f"WOAH! A CRITICAL HIT. You strike with all your power. You dealt 20 damage to the dragon leaving it with {dragon} hp")
            if dragon>=1:
                damaged = (random.randint(1,6))
                damaged += charge
                critd = (random.randint (1,100))
                if critd <= 5:
                    damaged *= 2
                player -= damaged
                if critd >= 6:
                    print(f"The dragon attacks, you took {damaged} and you now have {player} hp")
                else:
                    print(f"WATCH OUT! The dragon landed a critical hit and dealt {damaged} damage to you leaving you with {player} hp")
        else: #Failsafe in case someone types an invalid number
            print("Invalid move, try again")
    elif player >=1 and dragon <= 0: #Checks if you won the battle
        print("The dragon is defeated well done")
        quit()
    elif player <= 0 and dragon >= 1: #Checks if you lost the battle
        print("The dragon knocked you out. Game over")
        quit()
    else: # Failsafe incase something goes really wrong
        print("An error has occured closing game")
        quit()
    BigAttack = turn_count % 3 #How we check if the turn is a multiple of 3
    if turn_count >= 5 and comeback <= 4:
        cooldown += 1
    if turn_count == 5 or cooldown == 5:
        comeback = 10
    if BigAttack == 0 and dragon >= 1: #On turns which are a multiple of 3 increases the dragons damage
        charge = 3
        print("The dragon is readying its breath") #A small message to tell the player to look out 
    else:
        charge = 0 #Makes it so the dragons attacks won't deal increased damage on other turns

