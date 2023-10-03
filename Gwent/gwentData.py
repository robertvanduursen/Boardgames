"""
Gwent: Iron Judgement

Card and Faction data

"""


import json, re, sys, os



# root = r'C:\Users\rober\Google Drive\Games\Gwent\\'
import random

# root = r'C:\Users\rober\Google Drive\Games\Gwent\data\\'
root = os.path.join(os.path.dirname(__file__), 'data')


def categories():
    cats = json.load(open(root + '\categories.json'))

    for idx,(name,desc) in enumerate(cats.items()):
        print(idx, desc)
    return True


def printKeywords():
    words = json.load(open(root + '\keywords.json'))
    for idx,(name,desc) in enumerate(words.items()):
        print(idx, desc)

# printKeywords()

def keywords():
    words = json.load(open(root + '\keywords.json'))

    # for idx,(name,desc) in enumerate(words.items()):
    #     print(idx, name, desc['text'])
    return {name: desc for name, desc in words.items()}

allKeywords = keywords()

class Card(object):
    artist = False  # Anna Podedworna
    cardType = False  # Unit
    categories = False  # ['Witcher']
    categoryIds = False  # ['card_category_31']
    faction = False  # Neutral
    secondaryFaction = False  # Syndicate stuff
    flavor = False  # {'de-DE': 'Ich gehe, wohin und wann immer ich will.', 'en-US': 'I go wherever I please, whenever I please.', 'es-ES': 'Yo voy donde me apetece, cuando me apetece.', 'es-MX': 'Voy donde me da la gana, cuando me da la gana.', 'fr-FR': 'Moi, je vais où je veux, quand je veux.', 'it-IT': 'Posso andare dove voglio, quando voglio.', 'ja-JP': '私は好きな時に、どこへでも行けるの', 'ko-KR': '전 가고 싶을 때 어디로든 갈 수 있어요.', 'pl-PL': 'Ja mogę iść, gdzie chcę i kiedy chcę.', 'pt-BR': 'Eu vou aonde eu quiser, a hora que eu quiser.', 'ru-RU': 'А я могу идти где хочу и когда хочу.', 'zh-CN': '“去往何处，何时动身，我自己说了算。”', 'zh-TW': '去往何處，何時動身，我自己說了算。'}
    info = False  # {'de-DE': 'Nimm diese Einheit vom Schlachtfeld zurück auf die Hand, wann immer du eine Runde verlierst.\n', 'en-US': 'Whenever you lose a round, return this unit from the battlefield to your hand.\n', 'es-ES': 'Cada vez que pierdas una ronda, devuelve esta unidad del campo de batalla a tu mano.\n', 'es-MX': 'Siempre que pierdas una ronda, regresa esta unidad a tu mano desde el campo de batalla.\n', 'fr-FR': 'Chaque fois que vous perdez une manche, replacez la présente unité dans votre main.\n', 'it-IT': 'Ogni volta che perdi un round, riprendi in mano questa unità dal campo di battaglia.\n', 'ja-JP': 'あなたがラウンドに敗北するたび、戦場にあるこのユニットを自軍手札に戻す。\n', 'ko-KR': '라운드에서 패하면 전장에서 손으로 돌아온다.\n', 'pl-PL': 'Za każdym razem, gdy przegrasz rundę, cofnij tę jednostkę z pola bitwy do swojej ręki.\n', 'pt-BR': 'Sempre que você perder uma rodada, retorne esta unidade do campo de batalha para a sua mão.\n', 'ru-RU': 'Возвращайте этот отряд с поля в вашу руку каждый раз, когда проигрываете раунд.\n', 'zh-CN': '己方输掉小局时返回手牌。\n', 'zh-TW': '每當我方一局落敗，便從場上將此單位牌收回我方手牌。\n'}
    infoRaw = False  # {'de-DE': 'Nimm diese Einheit vom Schlachtfeld zurück auf die Hand, wann immer du eine Runde verlierst.\n', 'en-US': 'Whenever you lose a round, return this unit from the battlefield to your hand.\n', 'es-ES': 'Cada vez que pierdas una ronda, devuelve esta unidad del campo de batalla a tu mano.\n', 'es-MX': 'Siempre que pierdas una ronda, regresa esta unidad a tu mano desde el campo de batalla.\n', 'fr-FR': 'Chaque fois que vous perdez une manche, replacez la présente unité dans votre main.\n', 'it-IT': 'Ogni volta che perdi un round, riprendi in mano questa unità dal campo di battaglia.\n', 'ja-JP': 'あなたがラウンドに敗北するたび、戦場にあるこのユニットを自軍手札に戻す。\n', 'ko-KR': '라운드에서 패하면 전장에서 손으로 돌아온다.\n', 'pl-PL': 'Za każdym razem, gdy przegrasz rundę, cofnij tę jednostkę z pola bitwy do swojej ręki.\n', 'pt-BR': 'Sempre que você perder uma rodada, retorne esta unidade do campo de batalha para a sua mão.\n', 'ru-RU': 'Возвращайте этот отряд с поля в вашу руку каждый раз, когда проигрываете раунд.\n', 'zh-CN': '己方输掉小局时返回手牌。\n', 'zh-TW': '每當我方一局落敗，便從場上將此單位牌收回我方手牌。\n'}
    ingameId = False  # 112101
    keywords = False  # []
    loyalties = False  # ['Loyal']
    name = False  # {'de-DE': 'Ciri', 'en-US': 'Ciri', 'es-ES': 'Ciri', 'es-MX': 'Ciri', 'fr-FR': 'Ciri', 'it-IT': 'Ciri', 'ja-JP': 'シリ', 'ko-KR': '시리', 'pl-PL': 'Ciri', 'pt-BR': 'Ciri', 'ru-RU': 'Цири', 'zh-CN': '希里', 'zh-TW': '希里'}
    positions = False  # ['Melee', 'Ranged', 'Siege']
    provision = False  # 8
    related = False  # []
    released = False  # True
    strength = False  # 4
    type = False  # Gold
    variations = False  # {'11210100': {'art': {'high': 'https://firebasestorage.googleapis.com/v0/b/gwent-9e62a.appspot.com/o/images%2Fv3.1.0%2F112101%2F11210100%2Fhigh.png?alt=media', 'ingameArtId': '1007', 'low': 'https://firebasestorage.googleapis.com/v0/b/gwent-9e62a.appspot.com/o/images%2Fv3.1.0%2F112101%2F11210100%2Flow.png?alt=media', 'medium': 'https://firebasestorage.googleapis.com/v0/b/gwent-9e62a.appspot.com/o/images%2Fv3.1.0%2F112101%2F11210100%2Fmedium.png?alt=media', 'original': 'https://firebasestorage.googleapis.com/v0/b/gwent-9e62a.appspot.com/o/images%2Fv3.1.0%2F112101%2F11210100%2Foriginal.png?alt=media', 'thumbnail': 'https://firebasestorage.googleapis.com/v0/b/gwent-9e62a.appspot.com/o/images%2Fv3.1.0%2F112101%2F11210100%2Fthumbnail.png?alt=media'}, 'availability': 'BaseSet', 'collectible': True, 'craft': {'premium': 1600, 'standard': 800, 'upgrade': 400}, 'mill': {'premium': 200, 'standard': 200, 'upgrade': 120}, 'rarity': 'Legendary', 'variationId': '11210100'}}

    text = False

    def __init__(self, data= False):
        if data:
            self.__dict__ = data

            self.text = self.info


    def printStats(self):
        print(self.name)
        print(self.cardType)
        print(self.categories)
        print(self.info)
        print(self.keywords)
        print(self.positions)

    def getInfo(self):
        return self.info

    def isEngine(self):
        """
        check whether this card has the potential for being an engine or teaming up

        i.e. does it have an 'at the end of turn' or 'every time X happens'
        """

        if any([True for test in ['every', 'whenever'] if test in self.text.lower()]):
            if 'deploy' not in self.text.lower():
                return True
        return False

    def isPressurer(self):
        """ dd """
        if any([True for test in ['zeal'] if test in self.text.lower()]):
            return True
        return False

    def isToppler(self):
        """ the one that outperforms """
        if any([True for test in ['bloodthirst', 'berserk'] if test in self.text.lower()]):
            return True
        return False

    def isEffector(self):
        """ the one that outperforms """
        if any([True for test in ['when '] if test in self.text.lower()]):
            return True
        return False

    def isController(self):
        """ ability based """
        if any([True for test in ['order', 'deploy', 'charge'] if test in self.text.lower()]):
            return True
        return False


def loadCards():
    loadedCards = []
    cards = json.load(open(root + '\cards.json'))

    for idx,(cardNr,desc) in enumerate(cards.items()):
        #print(idx, cardNr)
        loadedCards.append(Card(desc))
    print('loading done')
    return loadedCards

allCards = loadCards()

# factions = set([card.faction for card in allCards])
# for idx, name in enumerate(factions):
#     print(idx, name)

# cardTypes = set([card.cardType for card in allCards])
# print(cardTypes)
# for idx, name in enumerate(cardTypes):
#     print(idx, name)
cardTypes = ['Unit', 'Leader', 'Strategem', 'Spell', 'Artifact']

class Faction:
    name = str
    cards = list
    Leaders = list
    Units = list
    Spells = list
    Artifacts = list
    Strategems = list

    keywords = list

    def __init__(self, name = False):
        if name: self.name = name
        self.cards = []
        self.Leaders = []
        self.Units = []
        self.Spells = []
        self.Artifacts = []
        self.Strategems = []
        self.keywords = []

    def addCard(self, card):
        self.cards.append(card)
        self.__dict__[card.cardType+'s'].append(card)
        self.keywords += card.keywords

        pass

    def __add__(self, other):
        mergedFaction = Faction()
        for name, val in self.__dict__.items():
            if isinstance(val,list):
                mergedFaction.__dict__[name] += val

        for name, val in other.__dict__.items():
            if isinstance(val,list):
                mergedFaction.__dict__[name] += val

        mergedFaction.name = self.name
        return mergedFaction

    def getCard(self, name):
        """ by name """
        if name in [card.name for card in self.cards]:
            return [card for card in self.cards if card.name == name][0]

        return False


    @property
    def playableCards(self):
        """ exclude token cards """
        return self.units + self.spells + self.artefacts

    @property
    def units(self):
        """ exclude token cards """
        return [card for card in self.cards if card.cardType == 'Unit' and 'Token' not in card.categories]

    @property
    def spells(self):
        """ spells are a Special card """
        return [card for card in self.cards if card.cardType == 'Spell']


    @property
    def artefacts(self):
        return [card for card in self.cards if card.cardType == 'Artifact']


    def uniquekeyWords(self):
        uniqueWords = set(self.keywords)
        #freq = [(word, self.keywords.count(word)) for word in sorted(uniqueWords)]
        freq = {word: self.keywords.count(word) for word in sorted(uniqueWords)}
        return freq

    def subSets(self):
        """ card that are subset or super sets of each other """
        # i.e. the more powerful versions
        for card in self.cards:
            ownInfo = card.getInfo()
            blankInfo = ''.join(['0' if char.isdigit() else char for char in ownInfo]).replace('\n',' ')
            # print(blankInfo)
            for other in set(self.cards) - {card}:
                otherInfo = other.getInfo()
                otherBlank = ''.join(['0' if char.isdigit() else char for char in otherInfo]).replace('\n',' ')
                if blankInfo in otherBlank:
                    print('\t', card.name, 'is same as', other.name)
                    print('\t', card.name, '=', card.getInfo()[:-1])
                    print('\t', other.name, '=', other.getInfo()[:-1])
                    print()



    def engines(self):
        total = 0
        for card in self.cards:
            if card.isEngine():
                #print(card.name)
                #print(card.info)
                total += 1
        #print(total)
        return total

    def doublers(self):
        total = 0
        for card in self.cards:
            if 'double' in card.info.lower():
                # print(card.name)
                # print(card.info)
                total += 1
        #print(total)
        return total


    def printDistri(self):
        for name, attr in self.__dict__.items():
            if isinstance(attr,list):
                print('\t%s = %s' % (name,len(attr)))

    def printKeywordDistri(self):
        uniqueWords = self.uniquekeyWords().keys()
        print("\t# %s keywords " % len(self.keywords))
        print("\t# %s abilities " % len(uniqueWords))
        print('\tkeywords = {')
        freq = [(word, self.keywords.count(word)) for word in sorted(uniqueWords)]
        for word, nr in sorted(freq, key= lambda x: -x[1]):
            print("\t\t'%s': %s,  # %s" % (word, nr, allKeywords[word]))
        print('\t}')





# load the factions
factionsNames = ['Neutral', 'Syndicate', 'Nilfgaard', 'Monster', 'Northern Realms', 'Scoiatael', 'Skellige']
# factions = ['Scoiatael']
Factions = {}
for faction in factionsNames:
    _faction = Faction(faction)
    for card in allCards:
        if card.faction == _faction.name or card.secondaryFaction == _faction.name:
            _faction.addCard(card)
    Factions[_faction.name] = _faction

    # print(_faction.name)
    # print(_faction.doublers())
    # print(_faction.subSets())

    # for card in _faction.cards: print(card.name[ 'en-US'],'\n',card.getInfo(),'\n')

    # print('engines', _faction.engines())

    # total = 0
    # for card in _faction.cards:
    #     if card.isController(): total += 1
    # print('Controllers', total)
    # total = 0
    # for card in _faction.cards:
    #     if card.isPressurer(): total += 1
    # print('Pressurers', total)
    # total = 0
    # for card in _faction.cards:
    #     if card.isEffector(): total += 1
    # print('Effectors', total)
    # total = 0
    # for card in _faction.cards:
    #     if card.isToppler(): total += 1
    # print('Topplers', total)
    # print()

    # _faction.printDistri()
    # _faction.printKeywordDistri()


def showUniqueAbility():
    """ show unique faction abilities """
    for faction in Factions.keys():
        uniqueAbilities = set(faction.keywords)
        for otherFaction in set(Factions) - {faction}:
            uniqueAbilities -= set(otherFaction.keywords)
        print(faction.name, len(uniqueAbilities), uniqueAbilities)

def printAllEngines():
    # print(loadedFactions[3].name,'\n')
    total = 0
    for faction in Factions.keys():
        for card in faction.cards:
            if card.isEngine():
                print(card.name)
                print(card.info)
                total += 1
    print(total)

# print([card for card in allCards if 'greatsword' in card.name.lower()][0].info)

def printStrengths():
    for card in sorted(allCards, key= lambda x: -x.strength):
        print(card.name, card.strength)

    strengths = [x.strength for x in allCards]
    strengthFreq = {strength: strengths.count(strength) for strength in set(strengths)}

    for item in strengthFreq.items():
        print(item)




'''
Cahir Dyffryn
Melee: Whenever an enemy receives a boost, boost self by the same amount.


Alba Pikeman
Melee: Every allied turn, on turn end, damage a random enemy unit on the melee row by 1.


Vran Warrior
Whenever a unit is destroyed during your turn, damage a random enemy unit by 1


She-Troll of Vergen
Melee: Whenever an allied unit is destroyed during your turn, boost self by 2.


Tridam Infantry
Whenever this unit receives a boost, damage a random enemy unit by 1.

Temerian Drummer
Every allied turn, on turn end, boost the unit to the right by 1.


Reynard Odo
Melee: Whenever you play a unit, boost it by 1.


Anna Strenger
Every allied turn, on turn end, boost the unit to the right by 1.
Inspired: Boost adjacent units by 1 instead.


Mahakam Defender
Every allied turn, on turn end, boost self by 1 if this unit is boosted.


Hawker Smuggler
Melee: Every allied turn, on turn end, boost a random unit in your hand by 1.

Xavier Moran
Melee: Whenever this unit receives a boost, boost it by an additional 2.


Blueboy Lugos
Whenever this unit takes damage, damage a random enemy unit by 2.



An Craite Longship
Melee: Whenever your opponent plays a unit, deal 1 damage to it.

An Craite Greatsword
Whenever an enemy unit on the opposite row takes damage, boost self by 1.

Dagur Two Blades
Melee: Whenever an enemy takes damage, boost self by 1.


Heymaey Flaminica
Every allied turn, on turn end, Heal all damaged allied units on this row by 1.


Artis
Ranged: Whenever a unit is played, damage it by half its current power.

Svalblod Priest
Every allied turn, on turn end, damage the allied unit to the right by 1, then boost self by 2.


'''


class Deck:
    deckFaction = False
    cards = list
    leader = False
    provisions = 150  # a resource that is taken up by cards

    def __init__(self):
        self.cards = []

    def randomDeck(self):

        self.deckFaction = Factions['Scoiatael']
        # can pick cards from 1 faction and Neutral
        combinedFaction = self.deckFaction + Factions['Neutral']
        # print(len(combinedFaction.cards))
        leaders = combinedFaction.Leaders
        self.leader = leaders[random.randrange(0, len(leaders))]
        self.provisions += self.leader.provision
        # print(self.leader.__dict__.items())

        # for card in gwentGame.Factions['Scoiatael'].cards:             print(card.name)

        self.buildDeck()


    def oneFaction(self):
        """
        can pick cards from 1 faction and Neutral
        """

    def downloadDeck(self, deckCode = False):
        test = r'https://www.playgwent.com/en/decks/3fedd07aa87077eec60f20b539019ad6'
        return test


    def buildDeck(self):
        while not self.min25Cards():
            randomCard = self.deckFaction.cards[random.randrange(0, len(self.deckFaction.cards))]
            self.addCard(randomCard)


    def addCard(self, card):
        """ this builds in the max 2 copies rule """
        if self.cards.count(card) > 2:
            pass
        else:
            self.cards.append(card)

    def min25Cards(self):
        """ you have at minimum 25 cards """
        if len(self.cards) >= 25:
            return True
        else:
            return False

    def max2Copies(self, card):
        """ is there a max number of copies? yes; 2x """
        if self.cards.count(card) > 2:
            return False
        else:
            return True

    def min13Units(self):
        """a valid deck must have at least 13 units """
        if len([card for card in self.cards if card.cardType == 'Unit']) < 13:
            return False
        return True

    def posProvisions(self):
        if self.provisions < 0:
            return False
        return True

    @property
    def valid(self):
        return max(True, self.min25Cards(), self.min13Units(), self.posProvisions())

    def validity(self):
        """ more verbose version of valid() """
        pass