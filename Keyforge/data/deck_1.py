import urllib.request,sys,os
import operator,os,re,sys,inspect # default imports
import sqlite3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#print(currentPath)

class actions:
    """ abilities """
    # and modelling implications through their triggering
    # both contextual to the game lore and mechanical actions


    def Play(self):
        """ when chosen and thus evaluated """
        pass

    def This(self):
        """ pointer to self when evaluated - contextual """
        pass

    def Card(self):
        """ fundamental means of play """
        pass

    def Creature(self):
        """ type of card """
        pass

    def Artifact(self):
        """ type of card """
        pass
    def Action(self):
        """ type of card and type of move """
        pass
    def Upgrade(self):
        """ type of card """
        pass
    def House(self):
        """ property of cards """
        pass
    def Key(self):
        """ object of winning - part of victory conditions """
        pass
    def Forge(self):
        """ turn aember into keys """
        pass
    def Armor(self):
        """ unit of defense """
        pass
    def Power(self):
        """ unit of strength """
        pass

    def Reap(self):
        """ ability / option to gain aember / increase aember count """
        pass

    def Damage(self): pass
    def Draw(self): pass
    def Deal(self): pass
    def Search(self): pass
    def Destroy(self): pass
    def Discard(self): pass
    def Fight(self): pass
    def Swap(self): pass
    def Attack(self): pass
    def Hazardous(self): pass
    def Taunt(self): pass
    def Chain(self): pass
    def Elusive(self): pass
    def Use(self): pass
    def Steal(self): pass
    def Archive(self): pass
    def Flank(self): pass
    def Omni(self): pass
    def Absorb(self): pass
    def Add(self): pass


    def Each(self): pass
    def Other(self): pass



    def Reveal(self): pass
    def Capture(self):
        """ get an aember and put it onto this card """
        pass
    def Purge(self): pass
    def Sacrifice(self): pass
    def Stun(self): pass
    def Heal(self): pass
    def Splash(self): pass
    def Skirmish(self): pass
    def Assault(self): pass
    def Destroyed(self): pass
    def Neighbor(self): pass
    def Turn(self): pass
    def Hand(self): pass
    def Deck(self): pass
    def Refills(self): pass
    def Return(self): pass
    def Ready(self): pass
    def Choose(self):
        """ one of many """
        pass
    def Current(self):
        """ now """
        pass

    def Exhaust(self):
        """ used and no longer usuable until reset / restored """
        pass
    def Friendly(self):
        """ your own """
        pass
    def Opponent(self):
        """ the human, the other party """
        pass
    def Enemy(self):
        """ directionality """
        pass
    def First(self):
        """ order / sequence """
        pass
    def May(self):
        """ optionality """
        pass
    def Gain(self):
        """ get / increase """
        pass
    def Aember(self):
        """ currency for actions, unit of progress, is turned into keys """
        pass

    def Time(self): pass
    def Dealt(self): pass   ## is in Deal
    def Get(self):
        """ get / increase / gains / receives """
        pass
    def Skip(self): pass
    def After(self): pass
    def During(self): pass
    def Next(self): pass
    def Cost(self): pass
    def Enter(self): pass
    def Active(self): pass
    def Lose(self):
        """ not yours anymore """
        pass
    def If(self):
        """ conditional """
        pass
    def You(self):
        """ you as Player """
        pass
    def Remainder(self):
        """ for the rest of """
        pass

    def Word(self): pass
    def Zone(self): pass
    def Unforge(self): pass
    def Trigger(self): pass
    def Trait(self): pass
    def Target(self): pass
    def Template(self): pass
    def Take(self): pass
    def Shuffle(self): pass
    def Repeat(self): pass
    def Poison(self): pass
    def Pick(self): pass
    def Pay(self): pass

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

    abilities = False

    def __init__(self):
        pass

    def parse(self):
        self.abilities = []
        text = self.CardText
        abilities = [item for item in actions.__dict__.keys() if item[0] != '_']
        #print(abilities)
        for ab in abilities:
            # todo: this only matches presence, not frequency
            if ab.lower() in text.lower():
                self.abilities.append(eval('actions.%s' % ab))



def loadCards():
    ''' Load cards '''
    conn = sqlite3.connect(r"../cards.db")
    schema = [i[1] for i in conn.execute("PRAGMA table_info('cards')").fetchall()]
    #print('schema',schema)
    result = []
    with conn:
        cardDb = conn.execute('SELECT * FROM cards')
        for row in cardDb:
            newCard = Card()
            newCard.__dict__ = {schema[idx]: row[idx] for idx in range(len(row))}
            result.append(newCard)
    return result


allCards = loadCards()

class Deck:
    name = 'none'
    set = 'call of the archons'
    cardList = {}
    cards = []

    def stats(self):
        """ print statistics """
        print('\n',self.name)
        nrCards = len(self.cards)
        print('nr Cards', nrCards)
        for mark in ['Creature', 'Action', 'Artifact', 'Upgrade']:
            marks = [card for name,card in self.cards if card.TypeAction == mark]
            print('nr %ss' % mark, len(marks),'=', round((len(marks) / nrCards)*100,2),'%')
        print()

        styles = [
            ('Aamber Givers', lambda card: card[1].Aember != '0'),
            ('Players', lambda card: 'play' in card[1].CardText.lower() and card[1].TypeAction != 'Action'),
            ('Triggered', lambda card: any([hit in card[1].CardText.lower() for hit in ['action:', 'reap:', 'fight:']])),
        ]

        abilities = [(item, "lambda card: '%s' in str(card[1].abilities)" % item) for item in actions.__dict__.keys() if item[0] != '_']
        ranking = []
        for name,func in styles + sorted(abilities):
            if isinstance(func,str):
                #print(func)
                func = eval(func)
            cards = list(filter(func, self.cards))
            #print(name, len(cards), ' ' * (15 - len(name)), [card[0] for card in cards])
            ranking.append([name,len(cards),[card[0] for card in cards]])

        for name,leng,cards in sorted(ranking,key= lambda x:-x[1]):
            print(name, leng, ' ' * (17 - len(name)), cards)
        print()

    def spotCombo(self):
        """ spot a combo in your deck """
        # this can be a cycle, a Two-Trigger
        pass


myDeck = Deck()
myDeck.name = 'Ayanga, the Aember-holder of Wasps'
myDeck.cardList = {
        10: ("Loot the Bodies", 1),
        15: ("Sound the Horns", 1),
        20: ("Banner of Battle", 2),
        24: ("Mighty Javelin", 2),
        30: ("Bumpsy", 1),
        38: ("King of the Crag", 1),
        39: ("Krump", 1),
        48: ("Troll", 1),
        49: ("Wardrummer", 1),
        50: ("Blood of Titans", 1),
        267: ("Bait and Switch", 1),
        269: ("Finishing Blow", 1),
        275: ("Miasma", 1),
        276: ("Nerve Blast", 1),
        285: ("Customs Office", 1),
        290: ("Seeker Needle", 1),
        296: ("Bad Penny", 1),
        305: ("Nexus", 1),
        306: ("Noddy the Thief", 1),
        314: ("Umbra", 2),
        316: ("Duskrunner", 1),
        323: ("Full Moon", 2),
        325: ("Key Charge", 1),
        327: ("Lost in the Woods", 1),
        339: ("Word of Returning", 1),
        352: ("Flaxia", 1),
        362: ("Mushroom Man", 1),
        363: ("Niffle Ape", 2),
        364: ("Niffle Queen", 1),
        367: ("Hunting Witch", 1),
        368: ("Witch of the Eye", 1)
    }

myDeck1 = Deck()
myDeck1.name = 'Roscomb, the Imp of Longlane'
myDeck1.cardList = {
    58: ("Fear", 2),
    59: ("Gateway to Dis", 1),
    60: ("Gongoozle", 1),
    62: ("Hand of Dis", 1),
    67: ("Mind Barb", 1),
    75: ("Lash of Broken Dreams", 1),
    84: ("Eater of the Dead", 1),
    88: ("Guardian Demon", 1),
    96: ("Shooler", 1),
    101: ("The Terror", 1),
    102: ("Tocsin", 1),
    108: ("Dimension Door", 1),
    110: ("Foggify", 2),
    117: ("Phase Shift", 1),
    122: ("Scrambler Storm", 2),
    124: ("Twin Bolt Emission", 1),
    137: ("Brain Eater", 1),
    139: ("Doc Bookton", 1),
    144: ("Quixo the 'Adventurer'", 2),
    152: ("Skippy Timehog", 1),
    267: ("Bait and Switch", 1),
    268: ("Booby Trap", 1),
    270: ("Ghostly Hand", 1),
    276: ("Nerve Blast", 1),
    280: ("Poison Wave", 2),
    281: ("Relentless Whispers", 1),
    301: ("Macis Asp", 1),
    306: ("Noddy the Thief", 1),
    307: ("Old Bruno", 1),
    311: ("Silvertooth", 1),
    316: ("Duskrunner", 1),
    }



def deckInfo(deck):
    """ prints stats and cards """
    cardDict = {card.Number: card for card in allCards if deck.set in card.Sets.lower()}
    for card in deck.cardList.items():
        nr = int(card[0])
        theCard = cardDict[nr]
        for x in range(card[1][1]):
            deck.cards.append((theCard.Name, theCard))
            theCard.parse()

    deck.stats()

    sorter = [
        lambda x: -len(set(x[1].abilities)),
        lambda x: -int(x[1].Aember),
    ]

    for name, card in sorted(deck.cards, key=sorter[1]): #TypeAction
        stat = ' -> %s Aember %s, %s,' % (len(card.abilities), card.Aember,card.TypeAction)
        print(card.Name,' ' * (17-len(card.Name)),stat,' ' * (25-len(stat)),'Text =', re.sub(r'<(.*?)>', '', card.CardText))

    return deck


if __name__  == '__main__':
    newInfo = deckInfo(myDeck)
    print()
    #deckInfo(myDeck1)

    #cname = 'Niffle Queen' #'Mighty Javelin' # 'Blood of Titans'
    #card = [card for name, card in newInfo.cards if name == cname][0]
    #print(card.abilities)

'''
cards have effects and properties that trigger to cause the transition to new states
you can use logic to determine whether you can reach a state -at all-
'''

