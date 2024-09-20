import numpy

num = [
    10,
    10,
    4,
    22,
    13,
    4,
    56,
    15,
]
print(num)
total = sum(num)
print(total) 
multiply = numpy.prod(num)
print (multiply)
num.sort()
print(num[0-1])
num = list(dict.fromkeys(num))
print(num)