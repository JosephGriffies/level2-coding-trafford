import random
import time
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
critrate = 10
well_trigger = 0
well_check = 0
key = 0
secret = 1
start = 0

print("THE SIN OF GREED")
time.sleep(2)
while start == 0:
    difficulty = input("Select your difficulty (1) Normal (2) Hard")
    difficulty = int(difficulty)
    if difficulty == 1 or difficulty == 2:
        start += 1
    else:
        print("Invalid input try again")

def fight(enemy, modifier, health,xp,charge,threat,tell): 
    print(f"Oh no a {enemy} has appeared")
    time.sleep(1)
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
    global critrate
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
                if critp <= critrate: #Chance for a critical hit
                    damagep *= 2 #If a critical hit happens doubles damage
                health -= damagep #What actually deals damage
                if critp > critrate:
                    print(f"You dealt {damagep} damage to the enemy leaving it with {health} hp")
                    time.sleep(2)
                else: 
                    print(f"WOAH! A CRITICAL HIT. You dealt {damagep} damage to the enemy leaving it with {health} hp")
                    time.sleep(2)
                valid = 1
            elif move == 2:
                turn_count += 1
                heal = (random.randint(3,9)) #decides how much hp to heal
                heal += healbuff
                player += heal #how hp is healed
                if player >= maxhp:
                    player = maxhp #fail safe to prevent healing over your max hp
                print (f"You healed yourself for {heal} and now you have {player}hp")
                time.sleep(3)
                valid = 1
            elif move == 3:
                turn_count += 1
                defend = (random.randint(1,6)) #decides how much to reduce damage by
                print(f"You raised your guard, the next attack will deal up to {defend} less damage")
                time.sleep(3)
                valid = 1
            elif move == 4 and comeback == 10 or cooldown == 5:
                turn_count += 1
                comeback += atkbuff
                critp = (random.randint(1,100))
                if critp <= critrate: #The comeback attack has a lower crit chance
                    comeback *= 2
                health -= comeback
                if critp > critrate:
                    print(f"You strike with all your power. You dealt {comeback} damage to the enemy leaving it with {health} hp")
                    time.sleep(3)
                    comeback = 0 #Means comeback can only be used once
                    cooldown = 0
                else: 
                    print(f"WOAH! A CRITICAL HIT! You strike with all your power. You dealt {comeback} damage to the enemy leaving it with {health} hp")
                    time.sleep(3)
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
                    time.sleep(2)
                else:
                    print(f"WATCH OUT! The {enemy} landed a crit and dealt {damaged} damage leaving you with {player} hp")
                    time.sleep(3)
        if turn_count >= 5 and comeback <= 4:
            cooldown += 1
        if turn_count == 5 or cooldown == 5:
            comeback = 10
        big_attack = turn_count % charge
        if big_attack == 0:
            print(tell)
            time.sleep(2)
    if player >=1 and health <= 0: #Checks if you won the battle
            print(f"The {enemy} is defeated and you gained {xp} xp")
            time.sleep(2)
            comeback = 0
            totalxp += xp
            if totalxp >= 20 and level !=7:
                level += 1
                atkbuff += 1
                healbuff += 1
                defbuff += 1
                maxhp += 10
                totalxp -= 20
                critrate += 2
                player = maxhp
                print("LEVEL UP! Your abilities are now stronger and your max hp is increased by 10")
            time.sleep(3)
    elif player <= 0 and health >= 1: #Checks if you lost the battle
        print(f"The {enemy} knocked you out. Game over")
        time.sleep(2)
        quit()
        
print("You've found yourself in a gloomy, damp cave. You can hear heavy footsteps behind you and it appears that you're being chased.")
time.sleep(3)
cave = 1
while cave == 1:
    direction = input("The path infront of you is split 2 ways.(1)Left (2)Right")
    direction = int(direction)
    if direction == 1:
        print("The path you have entered is dimly lit, you can hear water dripping down but you're not sure where it's coming from. ")
        cave = 0
        time.sleep(4)
    elif direction == 2:
        print("You have entered a dark, gloomy cave covered in spider webs. It smells damp and moldy.")
        cave = 0
        time.sleep(4)
    else:
        print("Invalid input")
print("You see the exit in the distance but before you can make it, an angry knight appears to block your path.")
time.sleep(4)
print("Stop! The king wants you dead!")
time.sleep(3)
if difficulty == 1:
    fight("Knight", -1, 15, 20, 50, 0, "You're bad at this.")
elif difficulty == 2:
    fight("Knight", 0, 30, 20, 5, 2, "I won't go easy on you!")
print("You have slain the kings knight, you can now exit the cave.")
time.sleep(3)
print("A large town stands before you. At the centre of the town you can see a large castle that almost seems as if it is looking down on the surroundings.")
time.sleep(5)
print("The people seem poor and like they are struggling to survive. It is likely that this is all the kings responsibility.")
time.sleep(4)
print("You should figure out how to get in to the castle so that way the king can pay for his negligence.")
time.sleep(3)

def garden ():
    global atkbuff
    global defbuff
    global healbuff
    print("In the center of the garden there was a large fountain surrounded by civillians.")
    time.sleep(4)
    print("The garden was lively, blooming with flowers, butterflies and trees.")
    time.sleep(3)
    flower = 1
    flower_garden = 1
    while flower_garden == 1:
        if flower == 1:
            garden_choice = input("What would you like to do?(1) Go back to the town, (2) Talk to the civilians, (3) Inspect the flowers")
        else:
            garden_choice = input("What would you like to do?(1) Go back to the town, (2) Talk to the civilians")
        garden_choice = int(garden_choice)
        if garden_choice == 1:
            print("You decide to return to town.")
            time.sleep(2)
            flower_garden = 0
            town()
        elif garden_choice == 2:
            print("You notice one of the civilians inspecting the flower field in the garden, they seem to be looking for something.")
            time.sleep(3)
            print("Greetings stranger, are you lost?")
            time.sleep(1)
            talk = 1
            while talk == 1:
                garden_talk = input("(1) What are you looking for? (2) Do you know anything about the well? (3) What are your thoughts on the king? (4) I'll be seeing you.")
                garden_talk = int(garden_talk)
                if garden_talk == 1:
                    print("Oh, nothing important. I heard that a flower in this field holds the power to enhance your abilites.")
                    time.sleep (3)
                    print("Is there anything else?")
                elif garden_talk == 2:
                    print("I heard that theres so many rats down there. They tend to avoid going to the left because the water is dirty.")
                    time.sleep (5)
                    print("Is there anything else.")
                elif garden_talk == 3:
                    print("Oh the king... He's been sending his knights to the town to steal money from the poor. Not many people like him around here.")
                    time.sleep (5)
                    print("Is there anything else.")
                elif garden_talk == 4:
                    print("Alright thanks, see you around.")
                    time.sleep (2)
                    talk = 0
                else:
                    print("I didn't catch that")
                    time.sleep(1)
                              
        elif garden_choice == 3 and flower == 1:
            print("You slowly walk up to the flower field and notice 3 shining flowers in the middle of the field.")
            time.sleep(3)
            buff = input("Which flower would you like to pick? (1) a red rose with sharp thorns(atk boost), (2) A lavendar known for its calming properties(healing boost), (3) A white cosmos known for its resillience (def boost)")
            buff = int(buff)
            if buff == 1:
                print("You feel stronger")
                atkbuff += 1
                flower = 0
                time.sleep(2)
            elif buff == 2:
                print("You feel as though you've learnt a lot about healing")
                healbuff += 1
                flower = 0
                time.sleep(2)
            elif buff == 3:
                print("You feel strong and resilient")
                defbuff += 1
                flower = 0
                time.sleep(2)
            else:
                print("You somehow missed all the flowers and picked up a strand of grass. It is useless. Maybe next time you'll pick up the correct thing")
                time.sleep(3)
        else:
            print("Input invalid, try again.")
              
            
            town() 

def town ():
    intown = 1
    global well_trigger
    global well_check
    while intown == 1:
        if well_trigger != 1 or well_check == 1:
            town_choice = input("What would you like to do?(1) Go to the garden, (2) Go to the castle gates, (3)Talk to the civilians, (4)Find an inn to rest at")
        else:
            town_choice = input("What would you like to do?(1) Go to the garden, (2) Go to the castle gates, (3)Talk to the civilians, (4)Find an inn to rest at, (5) Explore the suspicious well.")
        town_choice = int(town_choice)
        if town_choice == 1:
            intown = 0
            garden()
        elif town_choice == 2:
            intown = 0
            castle_gates()
        elif town_choice == 3:
            print("A strange man stands next to the well. He seems to be inspecting it.")
            time.sleep(2)
            print("Oh hello there stranger, can I help you with anything?")
            time.sleep(2)
            talk = 1
            while talk == 1:
                talk_town = input("(1) What's thee king like? (2)You seem to be inspecting that well, why? (3)Any recommendations, (4) I'll be seeing you")
                talk_town = int(talk_town)
                if talk_town == 1:
                    print("Oh well aren't you brave asking that out in public. Well if you ask me hes just not right. Ever since his corronation things haven't been the same.") 
                    time.sleep(6)
                    print("The people are poor and yet his castle just seems to get bigger and bigger.")
                    time.sleep(3)
                    print("Although between you and me I heard something strange about his castle gates and the number 3. Who knows what it stands for? Maybe some treasure? Nah thats probably just me being hopeful")
                    time.sleep(6)
                    print("Anything else I can do for ya")
                elif talk_town == 2:
                    print("Oh uh this well...  well between you and me I heard the knight dropped a key to the castle. I can't see it down there and the wells infested with rats so you'd have to be real brave to go in there")
                    time.sleep(8)
                    well_trigger = 1
                    print("Anything else I can do for ya?")
                elif talk_town == 3:
                    print("Well the inn is just lovely, always leaves me feeling energised. And I love relaxing in the garden. Those flowers make me feel stronger everytime I smell them.")
                    time.sleep(6)
                    print("Anything else I can do for ya")
                elif talk_town == 4:
                    print("Aight I'll be seeing ya, goodbye stranger")
                    time.sleep(2)
                    talk = 0
                else:
                    print("Sorry I didn't catch that?")
                    time.sleep(2)
        elif town_choice == 4:
            print("An inn stands before you its welcoming aura practically drags you inside")
            time.sleep(3)
            print("The atmosphere here is lively yet tiring, you decide to book a room for the night and go to sleep.")
            time.sleep(4)
            print("When you wake up in the morning you feel energised and ready to continue your mission")
            player = maxhp
            time.sleep(3)
            print(f"Your hp has been restored to {player}")
        elif town_choice == 5 and well_trigger == 1:
            print("You decide to inspect the well. It seems dark and grimy as though its been unused for years.")
            time.sleep(4)
            print("You notice a ladder leading to the bottom. Its time to retrieve the castle key.")
            time.sleep(4)
            well()

def well():
    print("You reach the bottom of the ladder and find before you are 3 branching paths.")
    time.sleep(3)
    x = 1
    while x <= 5:
        global well_check
        global key
        global well_trigger
        global difficulty
        print("A branching path appears before you.")
        time.sleep(2)
        well_choice = input("Which path would you like to take (1) Left (2) centre (3) right")
        well_choice = int(well_choice)
        ratwell = (random.randint(1,100))
        if  ratwell <= 20 and well_choice == 1:
            print("You take the left path and a rat approaches you. It is time to fight.")
            time.sleep(3)
            if difficulty == 1:
                fight("Rat", 1, 25, 10, 8, 2, "The rat squeaks aggresively")
            elif difficulty == 2: 
                fight("Rat", 2, 40, 10, 6, 3, "The rat squeaks aggresively")
            x += 1
        elif ratwell > 20 and well_choice == 1:
            print("You take the left path, it is clear.")
            time.sleep(2)
            x += 1
        elif  ratwell >= 60 and well_choice == 2:
            print("You take the centre path and a rat approaches you. It is time to fight.")
            time.sleep(3)
            if difficulty == 1:
                fight("Rat", 1, 25, 10, 8, 2, "The rat squeaks aggresively")
            elif difficulty == 2: 
                fight("Rat", 2, 40, 10, 6, 3, "The rat squeaks aggresively")
            x += 1
        elif ratwell < 60 and well_choice == 2:
            print("You take the centre path, it is clear.")
            time.sleep(2)
            x += 1
        elif  ratwell <= 60 and ratwell >= 20 and well_choice == 3:
            print("You take the right path and a rat approaches you. It is time to fight.")
            time.sleep(3)
            if difficulty == 1:
                fight("Rat", 1, 25, 10, 8, 2, "The rat squeaks aggresively")
            elif difficulty == 2: 
                fight("Rat", 2, 40, 10, 6, 3, "The rat squeaks aggresively")
            x += 1
        elif ratwell > 60 and ratwell < 20 and well_choice == 3:
            print("You take the right path, it is clear.")
            time.sleep(2)
            x += 1
        else:
            ("Invalid input try again")
    print("You find yourself surrounded in a grimy part of the well. Its practically glowing green.")
    time.sleep(3)
    print("You hear heavy footsteps approach you along with heavy dripping.")
    time.sleep(2)
    print("You turn around and see a giant mutated rat approaching you. As it lunges at you you realise it is time to fight.")
    time.sleep(4)
    fight("Mutated Rat", 2, 48, 20, 6, 3, "Acid is dripping from its fangs")
    print("You have defeated the mutated rat and around its neck you notice a key. It seems this will be how you enter the castle and take down the king.")
    time.sleep(4)
    well_check = 1
    well_trigger = 0
    key = 1
    town()

def castle_gates():
    print("Whilst walking towards the castle gates, you encounter a big intimidating wall.")
    time.sleep(2)
    global atkbuff
    global defbuff
    global healbuff
    global secret
    global difficulty
    gate = 1
    while gate == 1:
        if key != 1:
            print("There's nothing to do here right now. You decide to return to town")
            time.sleep(2)
            gate = 0
            town()
        elif key == 1:
            gate_choice = input("(1) Use the key to unlock the gates. (2) Return to the town") 
            gate_choice = int(gate_choice)
        if gate_choice == 1:
            print("You enter the castle gates to find an angry knight rushing towards you.")#haha comment
            time.sleep(3)
            print("You have some guts coming here!")
            time.sleep(2)
            if difficulty == 1:
                fight("Knight", 2, 50, 20, 6, 2,"The knight raises his shield")
            elif difficulty == 2:
                fight("Knight", 3, 70, 20, 7, 2,"The knight raises his shield")
            print("The Knight has been defeated.")
            time.sleep(2)
            print("Before you can catch your breath another knight angrily rushes towards you.")
            time.sleep(4)
            print("I WILL AVENGE MY COMRADE!")
            time.sleep(2)
            if difficulty == 1:
                fight("Knight", 2, 50, 20, 6, 2,"The knight raises his shield")
            elif difficulty == 2:
                fight("Knight", 3, 70, 20, 5, 2,"The knight raises his shield")
            print("After two tough fights, the captain slowly walks towards you in anger.")
            time.sleep(3)
            print("Do you think a weak peasant like you can defeat me?")
            time.sleep(2)
            if difficulty == 1:
                fight("Captain", 6, 70, 20, 5, 3,"The captain taunts you")
            elif difficulty == 2:
                fight("Captain", 7, 90, 20, 4, 4,"The captain taunts you")
            print("That seems to be the end of the knights, it is time to head to the throne room and make the king pay.")
            time.sleep(5)
            gate = 0
            throne_room()
        elif gate_choice == 2:
                gate = 0
                print("You decide to return to the town")
                time.sleep(2)
                town()
        elif gate_choice == 3 and secret == 1:
            print("You come across a variety of treasures, these should be helpful. You gain +1 to all your stats")
            secret = 0
            atkbuff += 1
            defbuff += 1
            healbuff += 1
            time.sleep(2)
        else:
            print("Invalid input, try again.")

def throne_room():
    final = 1
    print("You finally enter the throme room, it's massive and nothing like you've seen before.")
    time.sleep(4)
    print("At the top of the throne sits the greedy king. He starts shouting at you.")
    time.sleep(4)
    print("YOU FOOL! You think you can kill me? IM THE KING!")
    time.sleep(4)
    print("... Although you seem valuable to me, why dont we strike some sort of deal?")
    time.sleep(4)
    print("JOIN ME, and I'll give you all the riches in the world. You'll never struggle again!")
    time.sleep(4)
    while final == 1:
        throne_choice = input("(1) Reject the kings offer. (2) Accept the kings offer.")
        throne_choice = int(throne_choice)
        if throne_choice == 1:
            print("YOU FOOL! YOU DARE DISOBEY ME. I SHALL CUT YOU DOWN WHERE YOU STAND")
            final = 0
            time.sleep(3)
            if difficulty == 1:
                fight("King", 8, 90, 20, 4, 4, "The king laughs maniacally")
            elif difficulty == 2:
                fight("King", 9, 120, 20, 4, 4, "The king laughs maniacally")
            print("If you think this is the end of me you are mistaken. BLOOD HOUND, COME TO ME!!!")
            time.sleep(5)
            print("The wall behind the castle explodes and in the dust you see a figure of a dragon appear.")
            time.sleep(5)
            print("You shall not survive the combined wrath of me and my dragon")
            time.sleep(4)
            if difficulty == 1:
                fight("King and his Dragon", 9, 110, 999, 3, 2, "A fiery aura comes from the dragons mouth")
            elif difficulty ==2:
                fight("King and his Dragon", 10, 150, 999, 3, 2, "A fiery aura comes from the dragons mouth")
            print("No please don't kill me I'll make you rich! Please this doesn't have to be the end.")
            time.sleep(5)
            print("With a single slash of your blade the king is silenced. Permanently")
            time.sleep(4)
            print("It is now up to you to take the crown and help the people. Will you succeed as their ruler, or succumb to greed. It is now your path to walk")
            time.sleep(6)
            print("Thank you for playing!")
            time.sleep(1)
            quit()
        elif throne_choice == 2:
            print("THAT'S RIGHT! YOU WOULDN'T DARE DISOBEY THE KING!")
            time.sleep(3)     
            print("Just mere days after you accepted the kings offer the world got much worse. Whilst the king was filling your pockets with gold and silver, the poor were struggling to survive.") 
            time.sleep(7)   
            print("The king kept sending his knights out to slay the poor and take there food and supplies.")
            time.sleep(4)
            print("Thank you for playing!")
            time.sleep(1)
            final = 0
            quit()
        else:
            print("SPEAK UP WHEN YOU ARE TALKING TO ME!")
            time.sleep(1)

town()