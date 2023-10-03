"""

interface for Street Fighter 4 data

"""
from Fighters import *

#print(characters)



def useData():
    import urllib, sys, os
    import operator, os, re, sys, inspect  # default imports
    import xml.etree.cElementTree as ET

    currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    print(currentPath)

    allChars = []
    for char, parseName in characters.items():
        charName = char  # 'Akuma'
        char = Character(charName)
        char.load(parseName)
        allChars.append(char)

    maxDamage = [False, False]
    maxMoves = [False, False]
    fastestMoves = [False, False]
    avMoves = 0

    for char in allChars:
        #print(char.name)
        # char.printAllStats()
        avMoves += len(char.Moves)
        if len(char.Moves) > maxMoves[0]:
            maxMoves[0] = len(char.Moves)
            maxMoves[1] = char

        localMax = max([move.Damage for move in char.Moves])
        if localMax > maxDamage[0]:
            maxDamage[0] = localMax
            maxDamage[1] = char

        avSpeed = sum([move.totalSpeed for move in char.Moves]) / len(char.Moves)
        if avSpeed > fastestMoves[0]:
            fastestMoves[0] = avSpeed
            fastestMoves[1] = char

    print()
    print('avMoves =', avMoves / len(allChars))
    print('maxDamage =', maxDamage[0], maxDamage[1].name)
    print(maxDamage[1].getMeMax('Damage'))
    print('maxMoves =', maxMoves[0], maxMoves[1].name)

    print('fastestMoves =', fastestMoves[0], fastestMoves[1].name)



Juri = Fighter('Juri')

# Juri.getVitals(1)
Juri.load()
Juri.printAllStats()

def fighterQuery():
    fighters = [Fighter(char) for char in characters]

    ranking = [(char.name,char.getVitals()['Health']) for char in fighters]
    for name,stat in sorted(ranking,key=lambda x:-x[1]):
        print(name,stat)


'''
Health                950
Stun                  950
W-Ultra Scaling       75
Forward Walk Speed    0.035
Forward Dash Distance  1.41
Back Walk Speed       0.03
Forward Dash Total Frames  19
Back Dash Distance    1.2
Jump Height Apex      2.24
Back Dash Total Frames  27
Jump Total Frames     39
Back Dash Invincibility  8
Forward Jump Distance  1.7
Back Dash Airborne    10
Back Jump Distance    2.04
Back Dash Recovery    9
Forward Throw Range   0.83
Back Throw Range      0.83
Face Up Total Frames  31
Face Down Total Frames  21
Level 1 Focus Startup Frames  21
Level 2 Focus Startup Frames  29
Level 3 Focus Startup Frames  65
L1 Focus Attack Forward Dash  []
L2 FA Forward Dash (On Block)  []
L1 Focus Attack Back Dash  []
L2 FA Back Dash (On Block)  []
'''