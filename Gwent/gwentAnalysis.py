"""

rules of Gwent: Iron Judgement

"""

import gwentData, random
from gwentData import Deck

'''

two cards together can form an engine
i.e. combo


the one that loses a round, starts the next?

provisions man, provisions

'''

# for name in gwentGame.Factions: print(name)


if __name__ == '__main__' and 0:
    randDeck = Deck()
    randDeck.randomDeck()
    print(randDeck.valid)

    print('leader =', randDeck.leader.name, randDeck.leader.info)
    for idx, card in enumerate(randDeck.cards):
        print(idx, card.name)  # , card.faction)



class analyzeDeck:
    """ performance analysis """
    deck = False

    def synergy(self):
        """
        discover the synergy between card of Factions
        """

    def tactics(self):
        """
        optimal (play) order
        """

        options = [
            'forcing',
            'pressure',
            'outperform',
            'topple',
            'lock',
            'control',
        ]

        '''
        frequencies based on rules and constraints

        '''

    def diversity(self):
        """
        answers to scenarios
        """


    def bestDeck(self):
        """

        has answers to everything - V everything else
        mathematically balanced to fair well against everything else

        has great units

        can swing the score by big margins (easy comeback)

        has great synergy

        maximizes the card value (provision V card use ratio)

        card use ratio = effect, strength
        effect = better when it repeats

        playOrder = important for optimized play

        """

    def aggression(self):
        """ depends on level of damage dealing per turn """

    def frequencies(self):
        """ frequency / chance of drawing a specific card """

    def playOrder(self):
        """ Play order = determined by optimal play with current hand and board state
        Obviously, with a conflict game; this is re-evaluated every turn
        """


class cardQuality(gwentData.Card):
    """ get and extract information about a card """

    def __init__(self, card):
        self.__dict__.update(card.__dict__)

    def strengthRatio(self):
        if self.provision == 0 or self.strength == 0:
            return 0.0
        else:
            return round(self.strength / self.provision, 3)

    def risk(self):
        if self.cardType != 'Unit':
            return 0.0

        return 3.0 - self.strength # if its a Unit, its always at risk

    def value(self):
        val = self.strength
        if 'boost' in self.text.lower() and not 'enemy' in self.text.lower():
            # find the boost number
            pass

        if 'spawn' in self.text.lower() and 'copy' in self.text.lower():
            # print(self.text)
            # print(self.variations)
            pass

        # deconstruct logic consequences

        return val

    def ability(self):
        """ rank ability usefulness """
        value = 0.0

        # if its ability can repeat += 1.0
        if any([True for test in ['every', 'whenever'] if test in self.text.lower()]):
            if 'deploy' not in self.text.lower():
                value += 1.0

        # if it repeats every turn += 1.0
        if all([True for test in ['every', 'turn'] if test in self.text.lower()]):
            value += 1.0

        if all([True for test in ['damage', 'enemy'] if test in self.text.lower()]):
            value += 1.0

        if all([True for test in ['boost', 'self'] if test in self.text.lower()]):
            value += 1.0

        if all([True for test in ['boost', 'allied'] if test in self.text.lower()]):
            value += 1.0

        # means this card is limited
        if any([True for test in ['melee', 'ranged', 'deploy'] if test in self.text.lower()]):
            value -= 1.0

        if 'order' in self.text.lower() and 'charge' not in self.text.lower():
            value -= 1.0

        if 'order' in self.text.lower() and 'charge' in self.text.lower():
            value += 1.0

        # if it removes an opponent card from play += 1.0
        return value

    def synergy(self, cardSet):
        """ Label a cards synergy quality as how well it adds to the a selected set of cards. """
        '''
        This can then be:
            The entire faction + neutral + syndi
            OR
            the deck which it is in
        '''
        for card in cardSet:
            pass

    def optimal(self):
        """
        Quality:
            Optimal VS normal play
            A cards value normally = bare strength and effect that will always happen
            Optimal = effects that trigger when conditions are met
        :return:
        """

        # requires interpreter

    @property
    def quality(self):
        return self.ability() - self.risk() + self.strengthRatio() + self.value()


if __name__ == '__main__':
    print()

    combinedFaction = gwentData.Factions['Monster'] + gwentData.Factions['Neutral']
    # can pick cards from 1 faction and Neutral

    leaders = combinedFaction.Leaders
    leader = leaders[random.randrange(0, len(leaders))]
    provisions = leader.provision + 150

    qualities = [cardQuality(card) for card in combinedFaction.cards]
    for qual in sorted(qualities, key=lambda x: - x.quality):

        print(qual.name, '->', qual.quality)
        #, qual.strength, qual.provision

    # for fact, data in gwentGame.Factions.items():
    #     print()
    #     print(fact)
    #     for card in data.artefacts:
    #         print(card.name)


'''
Isengrim Faoiltiarna = intreresting in an all elf deck

milva = cool
'''