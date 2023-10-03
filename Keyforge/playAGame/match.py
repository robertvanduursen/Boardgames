""" a simulation of a match """
import random


class Action: pass


class Game:
    turnNumber = 0
    player1 = False
    player2 = False

    def __init__(self):
        self.prep()

        self.theTurn = self.Turn()
        print(next(self.theTurn))

        self.progress()
        self.progress()
        self.progress()
        self.progress()
        self.progress()
        self.progress()
        self.progress()
        self.progress()
        self.progress()

    def Turn(self):
        phases = ['start turn stuff','pick house','take archive','do actions','replenish cards','end turn']
        for step in phases:
            yield step

    def prep(self):
        return True


    def progress(self):
        try:
            print(next(self.theTurn))
        except StopIteration:
            print('\tnew turn')
            self.turnNumber += 1
            self.theTurn = self.Turn()

        #if self.theTurn.gi_running


class Board:
    pass


class Deck:
    cards = False
    def __init__(self):
        self.cards = []
        self.shuffle()


    def shuffle(self):
        random.shuffle(self.cards)


    def archive(self):
        pass


class Player:
    """
    players can do actions -> play card, draw card, fight, etc.
    players can make choices

    """
    aember = 0
    keys = 0

    def __init__(self,name='default', deck=False):
        self.name = name
        self._deck = deck
        self.handcards = []

    @property
    def deck(self):
        return self._deck

    @property
    def hand(self):
        return self.handcards



    def fight(self) -> Action:
        """ selected a creature and fight """
        # this function is implemented to simulate that a player
        # may want to fight, but hasnt realized that non of his creatures can


    def draw(self):
        self.handcards.append(self.deck.pop(0))


    def discard(self):
        pass

deck1, deck2 = True,True
player1, player2 = True,True


board = Board()
game = Game()

