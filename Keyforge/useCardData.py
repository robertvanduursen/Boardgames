import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import sqlite3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentPath)

class Card:
    Name = False
    CardText = False
    TypeAction = False
    House  = False
    Aember  = 0
    Power  = 0
    Armor  = 0
    rarity  = False
    Artist  = False
    FlavorText  = False
    Number  = 0
    Sets  = False
    InDecks  = False
    ADHD  = False

    def __init__(self):
        pass

class House:
    name = ''
    cards = False

    Creature = False
    Artifact = False
    Action = False
    Upgrade = False

    def __init__(self, name):
        self.name = name

        self.Creature = []
        self.Artifact = []
        self.Action = []
        self.Upgrade = []

    @property
    def numCards(self):
        return sum([len(x) for x in [self.Creature, self.Artifact, self.Action, self.Upgrade]])


    def stats(self):
        for typ in ['Creature', 'Artifact', 'Action', 'Upgrade']:
            cards = eval('self.%s' % typ)
            set1 = []
            set2 = []
            for card in cards:
                if card.Sets == ' Age of Ascension':
                    set1.append(card)
                else:
                    set2.append(card)

            print('\t{} {}: Age of Ascension has {} \n\t\t\tCall of the Archons has {}'.format(len(cards), typ, len(set1), len(set2) ))
        pass


Houses = {h: House(h) for h in ['Shadows', 'Mars', 'Logos','Untamed','Brobnar','Dis','Sanctum']}


def loadCards():
    ''' Load cards '''
    conn = sqlite3.connect("cards.db")
    schema = [i[1] for i in conn.execute("PRAGMA table_info('cards')").fetchall()]
    result = []
    with conn:
        cardDb = conn.execute('SELECT * FROM cards')
        for row in cardDb:
            newCard = Card()
            newCard.__dict__ = {schema[idx]: row[idx] for idx in range(len(row))}
            result.append(newCard)
    return result


allCards = loadCards()
#print(len(allCards))

for card in allCards:
    if card.TypeAction == 'Creature': Houses[card.House].Creature += [card]
    if card.TypeAction == 'Artifact': Houses[card.House].Artifact += [card]
    if card.TypeAction == 'Action': Houses[card.House].Action += [card]
    if card.TypeAction == 'Upgrade': Houses[card.House].Upgrade += [card]


def houseStats():
    for name, house in Houses.items():
        print(name, 'has %s cards' % (house.numCards))
        house.stats()
        print()

    creatureStats = sorted(Houses.values(),key=lambda h: len(h.Creature), reverse=True)
    print('{} has the most Creatures ({}) -> {} has the least ({})'.format(creatureStats[0].name, len(creatureStats[0].Creature), creatureStats[-1].name, len(creatureStats[-1].Creature)))

    artifactStats = sorted(Houses.values(),key=lambda h: len(h.Artifact), reverse=True)
    print('{} has the most Artifacts ({}) -> {} has the least ({})'.format(artifactStats[0].name, len(artifactStats[0].Artifact), artifactStats[-1].name, len(artifactStats[-1].Artifact)))

    actionStats = sorted(Houses.values(),key=lambda h: len(h.Action), reverse=True)
    print('{} has the most Actions ({}) -> {} has the least ({})'.format(actionStats[0].name, len(actionStats[0].Action), actionStats[-1].name, len(actionStats[-1].Action)))

    upgradeStats = sorted(Houses.values(),key=lambda h: len(h.Upgrade), reverse=True)
    print('{} has the most Upgrades ({}) -> {} has the least ({})'.format(upgradeStats[0].name, len(upgradeStats[0].Upgrade), upgradeStats[-1].name, len(upgradeStats[-1].Upgrade)))


abilityWords = [
    'card', 'creature', 'artifact', 'action', 'upgrade',
    'house', 'key', 'forge', 'armor', 'power',
    'damage', 'deal', 'search', 'destroy', 'discard',

    'play', 'fight', 'swap', 'attack', 'hazardous', 'taunt', 'chain', 'elusive', 'use', 'steal', 'archive', 'flank',
    'omni', 'reveal','capture', 'purge', 'sacrifice', 'stun', 'reap', 'heal', 'splash', 'skirmish',

    'destroyed', 'neighbor',
    #'turn', 'hand', 'deck', 'refills', 'return', 'ready', 'choose', 'exhaust',

    #'friendly', 'opponent', 'enemy', 'first',
    #'may', 'with', 'from', 'gain', #'time',

    #'dealt', 'skip', 'after', 'during', 'next', 'cost', 'enter', 'active',

]
#for x in abilityWords: print(x)

def wordFreq():
    words = []
    for card in allCards:
        words += [w.lower().strip() for w in card.CardText.split()]

    freqDict = sorted([(stat, words.count(stat)) for stat in set(words)], key=lambda x: x[1], reverse=True)
    for x in freqDict:     print(x)

def extractUsagePatterns(houses,words):
    """ using the common word and abilities, extract the frequency per house """

    houseFreq = {house: {word: 0 for word in words} for house in houses}

    for card in allCards:
        '''
        text = [w.lower().strip() for w in card.CardText.split()]
        text = set(text) & set(words)
        for word in text:
            houseFreq[card.House][word] += 1
        '''
        text = card.CardText.lower()
        for word in words:
            houseFreq[card.House][word] += text.count(word)

    return houseFreq

houseFreq = extractUsagePatterns(list(Houses.keys()), abilityWords)


def drawStats():
    ''' DRAAWWWWWWWW '''

    word_groups = len(abilityWords)
    fig, ax = plt.subplots(figsize=(70, 10))
    print(word_groups)  # 39
    index = np.arange(word_groups)
    bar_width = 0.1
    opacity = 0.7

    error_config = {'ecolor': '0.3'}

    clrs = ['k', 'm', 'b', 'g', 'r', 'c', 'y'] # 'w' m

    incr = 0
    for house in list(Houses.keys()):
        houseWords = tuple([houseFreq[house][w] for w in abilityWords])
        print(houseWords)
        rects1 = ax.bar(index + (bar_width*(incr+1))-(bar_width*3.5), houseWords, bar_width,
                        alpha=opacity, color=clrs[incr],
                        error_kw=error_config,
                        label=house)

        incr += 1


    ax.set_xlabel('words')
    ax.set_ylabel('freq')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(tuple(abilityWords))
    ax.legend()
    ax.axhline(10, color='grey', alpha=0.25)
    ax.axhline(1, color='grey', alpha=0.25)

    #fig.tight_layout()
    plt.savefig(r'C:\Users\rober\Google Drive\Games\Keyforge\wordFreq.png')

    plt.show()

drawStats()