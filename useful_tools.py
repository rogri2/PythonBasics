import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]

def getFileExt(filename):
    return filename[filename.index(".")+1:]

def rollDice(num):
    return random.randint(1, num)