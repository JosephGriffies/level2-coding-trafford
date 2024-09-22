1, 2, 3, 4, 5 ,6 ,7 ,8 ,9
2, 3, 4, 5, 6, 7, 8, 9,
2,4,5,6,7,8,9
2,4,6,7,8,9
2,4,6,8,9
2,4,6,8

list = [
    "Help"
    "Please"
    "Codewars"
    "Is"
    "Trying"
    "To"
    "Kill"
    "Me"
]

def remove_every_other(list):
    del list[1::2]
    return list

print (list)