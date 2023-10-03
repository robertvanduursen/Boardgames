"""
the board, the state

and how the presence or absence of a card changes that

"""

import gwentData
import gwentAnalysis



class Side:
    score = False
    leader = False

    meleeRow = list
    rangedRow = list

    graveyard = list

    def __init__(self):
        self.score = 0
        self.meleeRow = []
        self.rangedRow = []
        self.graveyard = []


    def addToMeleeRow(self, card):
        """ row moving = move to the right """
        if len(self.meleeRow) > 9:  # max 9 slots on board row
            pass
        else:
            self.meleeRow.append(card)
            self.score += card.strength

    def addToRangedRow(self, card):
        """ row moving = move to the right """
        if len(self.rangedRow) > 9:  # 9 cards on a row total
            pass
        else:
            self.rangedRow.append(card)

    @property
    def cards(self):
        return self.meleeRow + self.rangedRow


class Board:
    """ the gwent playing field """

    sideOne = Side
    sideTwo = Side


    @property
    def cardsInPlay(self):
        return self.sideOne.cards + self.sideTwo.cards

    def __init__(self, game):

        self.sideOne = Side()
        self.sideTwo = Side()

        self.scoreOne = 0
        self.scoreTwo = 0


class Player:
    """ an entity that can interact with the game and thereby change its state """
    _board = Board
    _game = False
    _name = False

    hand = list
    deck = list

    passed = False


    def __init__(self, name = False):
        if name: self._name = name
        self.deck = gwentData.Deck()
        self.deck.randomDeck()
        self.hand = []


    def playCard(self, card = False ):
        """ you can play 1 card per turn """
        playedCard = self.hand.pop(0)
        print('card played: "%s"' % (playedCard.name))
        self._board.sideOne.addToMeleeRow(playedCard)


    def drawCard(self):
        self.hand.append(self.deck.cards.pop(0))



    def endTurn(self):
        """ you can end your turn """

        # signal to game; end turn
        print('ending turn')
        self._game.nextTurn()

        # todo: the player should control the 'next turn' mechanic
        #  the game should facilitate it

    def passRound(self):
        """ you can pass the match (when?) """
        # at the beginning of a turn
        print('\n%s passed\n' % self._name)
        self.passed = True

        self.endTurn()


    def swapCards(self):
        """
        the opportunity to swap cards
        you can swap 2 cards after each match (3 @ round 1, 2 @ round 2)

        # you do not redraw cards after your turn
        """

        # these cards will the the first 3 cards you draw next

    def useLeader(self):
        """ you can use your leaders ability once per turn (depending on ability) """


class Gwent:
    """ the game """

    playerOne = False
    playerTwo = False
    round = 0
    turnNr = 1
    _board = Board
    _game = Board

    _activePlayer = False

    def __init__(self):
        self._board = Board(self)


    def startGame(self):
        self._activePlayer = self.playerOne
        self.startRound()

    def nextTurn(self):
        """ players play in turns """
        print('turn', self.turnNr, 'ended')
        self.turnNr += 1

        otherPlayer = self.playerTwo if self._activePlayer == self.playerOne else self.playerOne
        if not otherPlayer.passed:
            self._activePlayer = otherPlayer

        self.report()


    def nextRound(self):
        self.round += 1
        yield self.round

    def startRound(self):
        """ you start the match with 10 cards """

        for x in range(10):
            self.playerOne.drawCard()
        for x in range(10):
            self.playerTwo.drawCard()

        self.playerOne.swapCards()
        self.playerTwo.swapCards()

        # 15 cards

    def endRound(self):
        """ you draw 3 cards after each match """



    def report(self):
        """ report state of the game"""

        print('\nwere in turn number', self.turnNr)
        print('\tthe active player = %s' % self._activePlayer._name)
        print('\tscore = p1 %s  VS p2 %s' % (self._board.sideOne.score, self._board.sideTwo.score))

        print('\tplayer One has %s cards' % len(self.playerOne.hand))
        print('\tplayer Two has %s cards' % len(self.playerTwo.hand))


        # print(self.playerOne.hand)
        # print(self.playerTwo.hand)



game = Gwent()
playerOne = Player('playerOne')
playerTwo = Player('playerTwo')

# connecting
game.playerOne = playerOne
game.playerTwo = playerTwo

playerOne._game = game
playerTwo._game = game
playerOne._board = game._board
playerTwo._board = game._board


# demo game
game.startGame()

while game._activePlayer.hand:
    game._activePlayer.playCard()
    game._activePlayer.endTurn()

    if game.turnNr == 4: game._activePlayer.passRound()

print()
if game.playerOne._board.sideOne.score > game.playerTwo._board.sideTwo.score:
    print('player one wins!')
else:
    print('player two wins!')