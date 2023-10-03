
import gwentData, random



faction = gwentData.Factions['Monster'] + gwentData.Factions['Neutral']
# faction = gwentGame.Factions['Syndicate']

# can pick cards from 1 faction and Neutral
# combinedFaction = self.faction + gwentGame.Factions['Neutral']
# print(len(combinedFaction.cards))
# print(self.leader.__dict__.items())

# print(faction.getCard('Shupe: Hunter').cardType)
# raise

# for card in faction.playableCards:
#     print(card.name)
#     print(card.faction)
#     print(card.categories)
#     print(card.info)
# print(len(faction.playableCards))
#
# raise


from datetime import datetime

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
    allCards = faction.playableCards + faction.playableCards
    print('allCards in faction x 2: %s in %s' % (len(allCards), faction.name))
    allUnits = faction.units + faction.units  # double to incorporate <Max 2 copy rule>
    print('allUnits in faction x 2 ', len(allUnits))

    # remove Shupe's & tokens

    cardSet = allCards
    decks = []

    setSize = len(cardSet)
    steps = setSize - 24

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
            deck = [card for card, pick in zip(cardSet, cardIndexes) if pick]
            decks.append(deck)

        # if leftBehind == 2: break
    return decks


def clubStyleDecks():
    allCards = faction.playableCards + faction.playableCards
    print('allCards in faction x 2: %s in %s' % (len(allCards), faction.name))
    allUnits = faction.units + faction.units  # double to incorporate <Max 2 copy rule>
    print('allUnits in faction x 2 ', len(allUnits))


    cardSet = allCards

    decks = []
    for brack in range(20, 580):
        with open(r'C:\Users\rober\Google Drive\Experiments\Maths\clubOf25_%s.txt' % brack) as intCache:
            clubOf25 = eval(intCache.read())
            # print("subclub %s = %s big" % (brack,len(clubOf25)))
            for nr in clubOf25:
                deckMask = bin(nr)
                # print(deckMask)
                # if len(deckMask[2:]) > 500: print('debug')


                cardIndexes = [1 if by == '1' else 0 for by in deckMask[2:]]
                # print(len(cardIndexes))
                if sum(cardIndexes) == 25:
                    # print('cool')
                    deck = [card for card, pick in zip(cardSet, cardIndexes) if pick]
                    decks.append(deck)

    return decks


# todo: the whole 25 card set generated in 5 seconds; 406 possible cards
start = datetime.now()
allMonsterDecks = clubStyleDecks()
print("nr of decks = %s" % len(allMonsterDecks))
print('seconds:', (datetime.now() - start).seconds)

highestStrength, thatDeck = 0, []

# todo: previous count was 1139057
# todo: now count was 4277032


for idx, deck in enumerate(allMonsterDecks):
    deckStrength = sum([card.strength for card in deck])
    deckCost = sum([card.provision for card in deck])
    # print(idx, len(deck), deckCost)

    # if 'golyat' in str([card.name.lower() for card in deck]): print('KEWL')

    if 1 == 1: # deckCost <= 116:
        # print('WTF', deck)
        if deckStrength > highestStrength:
            highestStrength = deckStrength
            thatDeck = deck

print('\nhighestStrength', highestStrength)
for idx, card in enumerate(thatDeck):
    print(idx+1, card.name, card.strength)


"""
NOTE: a massive logical drawback in the Bit Marching approach = it will never split blocks
i.e. it can never make 000001110111000011100011
it has at most 2 blocks 00011111110000011 -> the marchers and the left behind

"""

"""
avenue:

is there a number theory, such that:
    "if this number is converted to a binary format; that it will have a specific number of positive bytes?"

"""