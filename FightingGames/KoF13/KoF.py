"""

interface for Street Fighter 4 data

"""
from Fighters import *


testChar = Fighter('Benimaru')
testChar.load()
for move in testChar.Moves:
    print(move.Name, move.__dict__)

# Mature.getMeMax('Active')

# for move in Mature.Moves:
#     print(move.Name, move.totalSpeed)

def useData():
    import operator, os, re, sys, inspect  # default imports

    allChars = []
    for char in characters.keys():
        try:
            charName = char  # 'Akuma'
            char = Character(charName)
            char.load()
            allChars.append(char)
        except:
            pass

    maxMoves = [0, False]
    fastestMoves = [100, False]
    avMoves = 0

    fastestMoves = []
    for char in allChars:
        #print(char.name)
        # char.printAllStats()
        avMoves += len(char.Moves)
        if len(char.Moves) > maxMoves[0]:
            maxMoves[0] = len(char.Moves)
            maxMoves[1] = char


        avSpeed = sum([move.totalSpeed for move in char.Moves]) / len(char.Moves)
        fastestMoves.append((char.name,avSpeed))

    fastestMoves = sorted(fastestMoves, key=lambda x: x[1])

    print()
    print('avMoves across all chars =', avMoves / len(allChars))
    print('maxMoves =', maxMoves[0], maxMoves[1].name)

    print('fastestMoves =', fastestMoves[0:3])

# useData()



def fighterQuery():
    fighters = [Fighter(char) for char in characters]

    ranking = [(char.name,char.getVitals()['Health']) for char in fighters]
    for name,stat in sorted(ranking,key=lambda x:-x[1]):
        print(name,stat)

