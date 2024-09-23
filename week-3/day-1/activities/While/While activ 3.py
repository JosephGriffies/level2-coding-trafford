import random
current_card = "fill"
cards = ["Diamond", "Spade", "Club", "Heart"]
find = random.choice(cards)
print (f"We want to find the card {find}")

while find != current_card:
    current_card = random.choice(cards)
    if current_card != find:
        print(f"It is a {current_card}, unfortunately we wanted a {find}")
    else:
        print(f"It is a {current_card}. This matches with the card we were trying to find")