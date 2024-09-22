import random
player = 30 #Players hp 
comeback = 0 #The value used to track when the superattack is ready and how much damage it will deal
cooldown = 0
critp = 100 
defend = 0
critd = 100 #above variables are established to prevent errors
level = 1
atkbuff = 0
defbuff = 0
healbuff = 0
maxhp = 30
totalxp = 0
big_attack = 0

def fight(enemy, modifier, health,xp,charge,threat,tell): 
    print(f"Oh no a {enemy} has appeared")
    global player
    turn_count = 1 #A way to track the turn count used for super attack
    global comeback
    global cooldown
    global atkbuff
    global defend
    global healbuff
    global level
    global maxhp
    global defbuff
    global totalxp
    global big_attack
    defend = 0
    while player >= 1 and health >= 1: #loops everything below until the code is closed
        if player >= 1 and health >= 1: #checks to see if the player and dragon are alive
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
                damagep += atkbuff
                if critp <= 10: #Chance for a critical hit
                    damagep *= 2 #If a critical hit happens doubles damage
                health -= damagep #What actually deals damage
                if critp >=11:
                    print(f"You dealt {damagep} damage to the enemy leaving it with {health} hp")
                else: 
                    print(f"WOAH! A CRITICAL HIT. You dealt {damagep} damage to the enemy leaving it with {health} hp")
                valid = 1
            elif move == 2:
                turn_count += 1
                heal = (random.randint(3,9)) #decides how much hp to heal
                heal += healbuff
                player += heal #how hp is healed
                if player >= maxhp:
                    player = maxhp #fail safe to prevent healing over your max hp
                print (f"You healed yourself for {heal} and now you have {player}hp")
                valid = 1
            elif move == 3:
                turn_count += 1
                defend = (random.randint(1,6)) #decides how much to reduce damage by
                print(f"You raised your guard, the next attack will deal up to {defend} less damage")
                valid = 1
            elif move == 4 and comeback == 10 or cooldown == 5:
                turn_count += 1
                comeback += atkbuff
                critp = (random.randint(1,100))
                if critp <= 5: #The comeback attack has a lower crit chance
                    comeback *= 2
                health -= comeback
                if critp >=6:
                    print(f"You strike with all your power. You dealt {comeback}) damage to the enemy leaving it with {health} hp")
                    comeback = 0 #Means comeback can only be used once
                    cooldown = 0
                else: 
                    print(f"WOAH! A CRITICAL HIT. You strike with all your power. You dealt {comeback} damage to the enemy leaving it with {health} hp")
                    comeback = 0 #Means comeback can only be used once
                    cooldown = 0
                valid = 1
            else:
                print ("Invalid move")
                valid = 0
            if valid == 1 and health >= 1:
                damaged = (random.randint(1,6))
                damaged += modifier
                if big_attack == 0:
                    damaged += threat
                critd = (random.randint(1,100))
                if critd <= 5:
                    damaged *= 2
                damaged -= defend
                defend = 0
                damaged -= defbuff
                if damaged <= 0:
                    damaged = 1
                player -= damaged
                if critd >= 6:
                    print(f"The {enemy} dealt {damaged} damage to you leaving you with {player} hp")
                else:
                    print(f"WATCH OUT! The {enemy} landed a crit and dealt {damaged} damage leaving you with {player} hp")
        if turn_count >= 5 and comeback <= 4:
            cooldown += 1
        if turn_count == 5 or cooldown == 5:
            comeback = 10
        big_attack = turn_count % charge
        if big_attack == 0:
            print(tell)
    if player >=1 and health <= 0: #Checks if you won the battle
            print(f"The {enemy} is defeated and you gained {xp}")
            totalxp += xp
            if xp >= 20 and level !=7:
                level += 1
                atkbuff += 1
                healbuff += 1
                defbuff += 1
                maxhp += 10
                totalxp -= 20
            print("LEVEL UP! Your abilities are now stronger and your max hp is increased by 10")
    elif player <= 0 and health >= 1: #Checks if you lost the battle
        print(f"The {enemy} knocked you out. Game over")
        quit()

print("Wow I sure hope I don't encounter an enemy")
fight("Rat", 2, 10, 30,20,0,"You're bad at this.")
print("Well that was scary I sure hope there aren't any Dragons around")
fight("Dragon", 2, 40, 20,6,3,"Don't defend this")