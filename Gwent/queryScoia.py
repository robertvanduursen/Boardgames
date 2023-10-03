
import gwentData, random



faction = gwentData.Factions['Scoiatael'] + gwentData.Factions['Neutral']
# faction = gwentGame.Factions['Syndicate']

# can pick cards from 1 faction and Neutral
# combinedFaction = self.faction + gwentGame.Factions['Neutral']
# print(len(combinedFaction.cards))
# print(self.leader.__dict__.items())


# for card in faction.cards:
#     print(card.name)
#     print(card.faction)
#     print(card.categories)
#     print(card.info)
#
# print(len(faction.cards))

# todo: the card set is incomplete

# todo: labels are also not complete, unless derived

# C:\Program Files (x86)\GOG Galaxy\Games\Gwent\Gwent_Data\StreamingAssets

# binary counting

def binCount(length=1):
    bitMask = eval("0b1%s" % ''.join(['0'] * length)) # length of array + 1 to prevent str byte compression
    # print(bitMask)
    for x in range(bitMask):
        yield x ^ bitMask

def str_binCount(length=1):
    bitMask = eval("0b1%s" % ''.join(['0'] * length)) # length of array + 1 to prevent str byte compression
    # print(bitMask)
    for x in range(bitMask):
        yield bin(x ^ bitMask)

# t = binCount()
# for x in range(20):
#     byte = next(t)
#     end = list(byte[3:])
#     print(end)


def gen_FactionDecks():
    allCards = faction.cards + faction.cards
    print('allCards in faction x 2', len(allCards))
    allUnits = faction.Units + faction.Units  # double to incorporate <Max 2 copy rule>
    print('allUnits in faction x 2 ', len(allUnits))
    counter = str_binCount(len(allUnits))

    min13Decks = 0
    for possibleDeck in range(len(allUnits)*len(allUnits)):
        deckMask = next(counter)
        # print(deckMask)
        # deckBytes = (deckMask).to_bytes(len(allCards)+1, byteorder='big')
        # # print(deckBytes)
        # print([1 if by else 0 for by in deckBytes])
        cardBytes = [1 if by == '1' else 0 for by in deckMask[3:]]
        # # cardBytes = list(bin(deckMask)[3:])
        # # # print(cardBytes)
        # #
        deck = [card for card, pick in zip(allUnits, cardBytes) if pick]


        if len(deck) > 13:  # valid Deck as <min 13 units rule>
            # print(len(deck))
            # print(sum(deckBytes[1:]), len(deck))
            min13Decks += 1
            pass

    print('nr min13Decks:', min13Decks)


'''
metrics:
took ~6 seconds to mine 164836 possibilities for 955 valid decks by binary counting

estimates put the number of 13 cards decks @ 6707070370505570470821559503360000

'''

from datetime import datetime


def mathProof():
    """
    proof for the "minimum 13 units = valid deck" rule

    ( all Cards in faction x 2 = 628 )
    ( all Units in faction x 2 = 406 )
    ( 64.6 % of the faction = Units )

    203 different unit

    allUnits = 406

    a minimum of 13 positive bits in the 406 bits deep array = a valid deck

    what portion is 13+ positive bits?

    the 13th power of 2 in positive form = 8191 (1 + 2 + 4 + 8 ...) = 1111111111111

    so everything before 8191 = not valid per definition?

    406 x 1's as a binary array to Int = 165263992197562149737978827008192759957101170741070304821162198818601447809077836456297302609928821211897803006255839576063
    ( 123 digits )

    406 - 13 = 393

    from a 406 deep bit array; how to select every variant of this array that has 13 positive bits?

    """

def powerOf2(seed):
    return pow(seed, 2)

start = 2
for x in range(1, 14):
    lol = ['1'] * x
    print(x, 'x 1s =', eval('0b%s' % ''.join(lol)))

    # print(eval())
    # start = powerOf2(start)


def revFac():
    """ test """

    def reverseFactorial(decr):
        decr = decr - 1
        return decr

    start = 203
    temp = 203
    for x in range(13):
        print(start, temp)
        start = reverseFactorial(start)
        temp = start * temp


'''
double card decks
406 406
405 164430
404 66429720
403 26771177160
402 10762013218320
401 4315567300546320
400 1726226920218528000
399 688764541167192672000
398 274128287384542683456000
397 108828930091663445332032000
396 43096256316298724351484672000
395 17023021244937996118836445440000

394 6707070370505570470821559503360000

single card decks
203 203
202 41006
201 8242206
200 1648441200
199 328039798800
198 64951880162400
197 12795520391992800
196 2507921996830588800
195 489044789381964816000
194 94874689140101174304000
193 18310815004039526640672000
192 3515676480775589115009024000

191 671494207828137520966723584000
'''

def showPerms():
    import math
    print()
    print('math.factorial(13)',math.factorial(13))
    print('math.factorial(203)',math.factorial(203))
    print('math.factorial(406)', math.factorial(406))
    print('pow(406,2)', pow(406,2))

    print((6707070370505570470821559503360000 / 164836) * 6)


def bitWalker():

    decks = []

    setSize = 203
    steps = setSize - 24
    print(pow(steps, 2))
    # this essentially does steps ^ 2
    for leftBehind in range(24):
        pass
        marcher = eval("0b%s" % ''.join(['1'] * (25-leftBehind)))
        marcher = (marcher << leftBehind)  # todo: add start offset

        bitArray = eval("0b1%s" % ''.join(['0'] * setSize))  # length of array + 1 to prevent str byte compression

        theLeftBehind = 0
        if leftBehind != 0:
            theLeftBehind = eval("0b%s" % ''.join(['1'] * leftBehind))

        # print(bin(marcher))
        # print(bin(theLeftBehind))
        # print()
        for x in range(leftBehind, steps):
            marched = marcher << x
            # print(marched, bin(marched))
            deckMask = marched ^ bitArray
            if leftBehind != 0:
                deckMask = deckMask ^ theLeftBehind
            deckMask = bin(deckMask)

            cardIndexes = [1 if by == '1' else 0 for by in deckMask[3:]]
            decks.append(cardIndexes)

        if leftBehind == 2: break

    # print(len(decks))
    # for x in range(5):
    #     print(decks[x])




def gen_FactionDecks():
    allCards = faction.cards + faction.cards
    print('allCards in faction x 2', len(allCards))
    allUnits = faction.Units + faction.Units  # double to incorporate <Max 2 copy rule>
    print('allUnits in faction x 2 ', len(allUnits))


    decks = []

    setSize = len(allUnits)
    steps = setSize - 24
    print(pow(steps, 2))
    # this essentially does steps ^ 2
    for leftBehind in range(24):
        pass
        marcher = eval("0b%s" % ''.join(['1'] * (25-leftBehind)))
        marcher = (marcher << leftBehind)  # todo: add start offset

        bitArray = eval("0b1%s" % ''.join(['0'] * setSize))  # length of array + 1 to prevent str byte compression

        theLeftBehind = 0
        if leftBehind != 0:
            theLeftBehind = eval("0b%s" % ''.join(['1'] * leftBehind))

        for x in range(leftBehind, steps):
            marched = marcher << x
            # print(marched, bin(marched))
            deckMask = marched ^ bitArray
            if leftBehind != 0:
                deckMask = deckMask ^ theLeftBehind
            deckMask = bin(deckMask)

            cardIndexes = [1 if by == '1' else 0 for by in deckMask[3:]]
            deck = [card for card, pick in zip(allUnits, cardIndexes) if pick]
            decks.append(deck)

        # if leftBehind == 2: break
    return decks


start = datetime.now()
print('gen_FactionDecks', len(gen_FactionDecks()))
print('seconds:', (datetime.now() - start).seconds)

# todo: the whole 25 card set generated in 5 seconds; 406 possible cards

allUnitDecks = gen_FactionDecks()
highestStrength, thatDeck = 0, False

for idx, deck in enumerate(allUnitDecks):
    deckStrength = sum([card.strength for card in deck])
    # print(idx, deckStrength)

    if deckStrength > highestStrength:
        highestStrength = deckStrength
        thatDeck = deck

print('\nhighestStrength', highestStrength)
for idx, card in enumerate(thatDeck):
    print(idx, card.name, card.strength)