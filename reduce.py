# Uso con reduce
from functools import reduce

myList = [2, 2, 2, 2, 2]
allMultiplied = reduce(lambda a, b: a * b, myList)
print(allMultiplied)