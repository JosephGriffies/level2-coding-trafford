objects = [
    "Chair",
    "Table",
    "Cup",
    "Pen",
]

games = [
    "Splatoon",
    "Pokemon",
    "The Legend of Zelda"
]

print(objects)

x = objects.count("Chair")
print(f"The object Chair comes up {x} times")

objects.extend(games)
print(objects)

objects.remove("Pokemon")
print(objects)

objects.reverse()
print(objects)

objects.sort()
print(objects)

