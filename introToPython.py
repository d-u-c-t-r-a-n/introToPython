
# Why Python?
# High-level programming
# Strong community (libraries/packages)


# Python vs other languages (1997)
# https://www.python.org/doc/essays/comparisons/
# Easy to write, slow run time

# Variables:
# No need to declare variable types. 
# Python automatically check for types on run time (Dynamic Typing)
# LHS = pointer, RHS = object with information
# Variables can be reused (just point to new object)
# ---------------------------------------------------------------------
# Data types:
# string, int, float, boolean, list, set, dictionary

# string
myVariable = "Hello World - Bonjour le monde"
print(myVariable)
myVariable = 13 + 45
print(myVariable)

# No semicolon needed. But we can still put it if we want to.

# numeric
wife = 1                # int
allowance = 23.45       # float
print(type(allowance))  # python default = float

# boolean
pythonIsFun = True
pythonIsHard = False

# collection
valuables = list()
belonging = ["socks", "shirts", 1, 23.45, ["pringles", "pepsi"]]
print(valuables)
print(belonging)

stores = tuple()
stores = ("Home Depot", "Tim Hortons", 99.99)

fruits = set()
fruits = {"Tomato", "Cucumber", "Beans", 3}

avgHousePrice2022 = dict()
avgHousePriceSep21 = {"British Columbia": 913471,
                      "Ontario": 887290,
                      "Calgary": 460100,
                      "Quebec": 459955,
                      "Alberta": 401705,
                      "Nova Scotia": 356757,
                      "Prince Edward Island": 335202,
                      "Newfoundland and Labrador": 321700,
                      "Manitoba": 321504,
                      "Saskatchewan": 286600,
                      "New Brunswick": 262200,
                      "Yukon": "Unknown",
                      "Nanavut": "Unknown",
                      "Northwest Territories": "Unknown",
                      3: dict()}

avgHousePriceSep21["Ontario"] = 23.45
print(avgHousePriceSep21)

# Manipulation:
me = "I don't eat dogs"
neighbor = me[8:] + " for fun"
print(neighbor)

alphabet = ["a", "b", "c"]
reversedAlphabet = alphabet[::-1]
print(reversedAlphabet)
# slicing syntax
# [<first element to include> : <first element to exclude> : <step>]

# Type casting
a = 5
b = str(5)
c = float(a)
d = int(b)

# condition
vous = 9
moi = 5
if vous > moi or vous == moi:
    print("indentation requires after \" : ")  # escape \
    print("replace curly braces ")
    if True:
        pass
elif vous <= moi and vous != moi:
    print("Or we can have one line statement")
else:
    print("Hello! My name is Duc")

# Ternary Operators
condition = True
statement = "Satisfied" if condition else "Not Satisfied"

# for loop
print("")
for i in range(len(belonging)):
    print(belonging[i])

for _ in range(5):
    print("Who let the dog out")

# while loop
counter = 0
while counter < 10:
    if counter == 2:
        counter += 2
        continue
    if counter == 6:
        break
    print(counter)
    counter += 1

# functions
def sum(a, b):
    return a+b

# class
class Person:
    def __init__(self, nameParam, ageParam):
        self.name = nameParam
        self.age = ageParam
    def getOld(self):
        self.age += 1
    def __str__(self):
        return self.name + " is " + str(self.age) + " years old."

duc = Person("Duc", 5)
duc.getOld()
print(duc)


# list comprehension
original = [x for x in range(20)]
print(original)

doubleEven = [x*2 for x in original if x % 2 == 0]
print(doubleEven)


# How Python helps me create synthetic data in Redgate
# PRCDCU = 8 digits
# 2x Province code in [10, 11, 12, 13, 24, 35, 46, 48, 59, 60, 61, 62]
# 2x Census Division sequentially
# 4x Collection Unit sequentially

import random
def pickProvinceCode():
    return random.choice(
        [10, 11, 12, 13, 24, 35, 46, 48, 59, 60, 61, 62])
print(pickProvinceCode())

def createPRCDCU(numRow):
    censusDivision = 1
    collectionUnit = 1

    for _ in range(numRow):
        result = int(str(pickProvinceCode()) +
                     str(censusDivision).zfill(2) + str(collectionUnit).zfill(4))
        collectionUnit += 1

        if collectionUnit > 9999:
            censusDivision += 1
            collectionUnit = 1

        yield result

print(list(createPRCDCU(10000)))



