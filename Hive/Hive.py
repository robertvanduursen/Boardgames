""" Py-Model of the board game Hive """
'''
Question: how interact with this code?

- I should be able to use this to test assumptions, stats and tactics

- It should be able to be used to model and verify a live structure as being the game Hive

- it should be able to answer: I have this Board State & these Pieces: what is the best move and why

- in a way it would be cool to be able to model this as a base for AI players to play and for a Human to join in


'''
# Note
#  What can I do in Game X? - what is the game about? whats the meta/story?
#  What are the rules of Game X? - how does one play?
#  What is the best strategy if I want X,Y,Z? this imparts meta-conditions on your system
#   for this reason, the code below needs to be interactable with comparitors
#   if you can only take 1 action; there is only 1 best advice

class Condition:
    """ dd """
class Rule:
    """ dd """

class Board:
    """ The hive """
    pieces = []
    connections = []
    game = False

    def __init__(self,game):
        self.game = game
        pass

    def setup(Condition):
        """ Each player takes all 11 pieces of one color and places them face up in front of them."""
        print('The board has been set up')


    @property
    def VALID(self):
        if endofTheGame(self.state):
            #quit
            #self.game.Over()
            print('end of game?')
            return False
            #self.Stop()
        noErrors = True
        if noErrors:
            return True
        return False

    @property
    def state(self):
        ''' check the state of the board to see if anyone won'''
        return (self.pieces,self.connections)


class Move:
    nrOfSteps = 0

## The Creatures ##
class Creature:
    """ prototype Insect """
    move = False
    position = False

    def __init__(self,pos=None):
        self.position = pos
        self.move = Move()

    def returnAdjecentSlots(self):
        return True

    def doMove(self):
        return None

    def suggestMove(self):
        """ a way to verify suggested moves for validity """
        return self.move

    def validMove(self):
        """ a way to verify suggested moves for validity """

class QueenBee(Creature):
    """
    The Queen Bee can move only one space per turn.
    Even thought it is restricted in this way, if moved at the right time it can severely disrupt your opponent's plans.
    """
    def __init__(self):
        super().__init__()
        self.move.nrOfSteps = 1

class Beetle(Creature):
    """
    The Beetle, like the Queen Bee, moves only one space per turn.
    Unlike any other creature though, it can also move on top of the Hive.
    A piece with a beetle on top of it is unable to move and for the purposes of the placing rules, the stack takes on the color of the Beetle.
    From its position on top of the Hive, the Beetle can move from tile to tile across the top of the Hive. It can also drop into spaces that are surrounded and therefore not accessible to most other creatures.
    From its position, the white Beetle is able to move into one of four positions.
    The only way to block a Beetle that is on top of the Hive is to move another Beetle on top of it. All four Beetles can be stacked on top of each other.
    Note When it is first placed, the Beetle is placed in the same way as all other pieces. It can't be placed directly on top of the Hive, even though it can be moved there later.
    """
    def __init__(self):
        self.move.nrOfSteps = 1

class Grasshopper(Creature):
    """
    The Grasshopper does not move around the outside of the Hive like the other creatures. Instead, it jumps from its space over any number of pieces (but at least one) to the next unoccupied space along a straight row of joined pieces.
    This gives it the advantage of being able to fill in a space which is surrounded by other tiles.
    From its position, the white Grasshopper can jump to one of three spaces. Note: It can't jump across the gap to the space marked x.
    """
    def __init__(self):
        self.move.nrOfSteps = 1


class Spider(Creature):
    """
    The Spider moves three spaces per turn - no more, no less.
    It must move in a direct path and can't backtrack on itself. It may only move around pieces that it is in direct contact with on each step of its move and it may not move across to a piece that it's not in direct contact with.
    From its position, the black Spider can move into one of four spaces but is unable to move to the position on its left marked 2 on its first step.
    """
    def __init__(self):
        self.move.nrOfSteps = 1


class SoldierAnt(Creature):
    """ This freedom of movement makes the Ant one of the most valuable pieces. """
    def __init__(self):
        #print('made ant')
        super().__init__() # == super(SoldierAnt,self).__init__()
        self.move.nrOfSteps = -1 # infinite

    @property
    def nrOfSteps(self):
        # this is more like a silly convenient bypass
        return self.move.nrOfSteps

    def validMove(self):
        """ The Soldier Ant can move from its position to any other position around the Hive provided the restrictions are adhered to. """
        if self.position != 'in between bits':
            return True
        else:
            return False

print('SoldierAnt',SoldierAnt().nrOfSteps)

class LadyBug(Creature):
    """
    The Ladybug pieces can be added to a standard Hive set and are placed in the same way as other pieces.
    Once in play, the Ladybug moves exactly three paves, two on top of the hive, then one down on its last move.
    It may not move around the outside of the Hive and may not end its move on top of other pieces; it can move into or out of surrounded spaces.
    """
    def __init__(self):
        self.move.nrOfSteps = 1

    def validMove(self):
        pass

class Mosquito(Creature):
    """
    Once in play, a Mosquito can take on the movement ability of any creature of either color that it is touching at the start of its move (a stack with a Beetle on top counting as a Beetle for this purpose), thus changing its movement characteristics throughout the game.
    Exceptions: If a Mosquito is only touching another Mosquito at the start of its move, it may not move at all. If a Mosquito is moved as a Beetle onto the top of the Hive, then it continues to move as a Beetle until it climbs down.
    """
    def __init__(self):
        self.move.nrOfSteps = 1

class Pillbug(Creature):
    """
    The Pillbug pieces can be added to a standard Hive set and are placed in the same way as other pieces.
    The Pillbug moves like the Queen Bee - one space at a time - but it also has a special ability that it may use instead of moving.
    This ability allows the Pillbug to move an adjacent un-stacked piece (whether friendly or enemy) two spaces: up on to the Pillbug itself, then down into an empty space adjacent to itself.
    #Exceptions:

        The Pillbug may not move the piece most recently moved by the opponent.
        The Pillbug may not move any piece in a stack of pieces.
        The Pillbug may not move a piece if it splits the hive (violating the One Hive Rule).
        The Pillbug may not move a piece through a too-narrow gap of stacked pieces (violating the Freedom to Move Rule).

    Any piece which physically moved (directly or by the Pillbug) is rendered immobile on the next player's turn; it cannot move or be moved, nor use its special ability. The mosquito can mimic either the movement or special ability of the Pillbug, even when the Pillbug it is touching has been rendered immobile by another Pillbug.
    """
    def __init__(self):
        self.move.nrOfSteps = 1



# Restrictions

class OneHiveRule(Rule):
    """
    The pieces in play must be linked at all times. At no time can you leave a piece stranded (not joined to the Hive) or seperate the Hive in two.
    Use this rule to your advantage by moving your pieces to strategic positions around the Hive, leaving your opponent's key pieces unable to move.
    Moving the black Queen Bee to a position where it re-links the Hive is also an illegal move as the Hive is left unlinked while the piece is in transit.
    """


class FreedomToMove(Rule):
    """
    The creatures can only move in a sliding movement. If a piece is surrounded to the point that it can no longer physically slide out of its position, it may not be moved.
    The only exceptions are the Grasshopper, which can jump into or out of a space, and the Beetle, which can also climb up or down.
    Similarly, no piece may move into a space that it can't physically slide into.
    When first introduced to the game, a piece may be placed into a space that is surrounded as long as it does not violate any of the placing rules, in particular the rule about pieces not being allowed to touch pieces of the other color when they are first placed.
    """

class UnableToMoveOrToPlace(Rule):
    """
    If a player can nether place a new piece or move an existing piece, the turn passes to their opponent who then takes their turn again.
    The game continues in this way until the player is able to move or place one of their pieces, or until the game is lost iwth the surrounding of their Queen Bee.
    """


def endofTheGame(board):
    """
    The game ends as soon as one Queen Bee is completely surrounded by pieces of any color.
    """
    print(board)
    pieces,connections = board
    if QueenBee not in [c.__class__ for c in pieces]:
        return False
    return True


'''
class endofTheGame(Rule):
    """
    The game ends as soon as one Queen Bee is completely surrounded by pieces of any color.
    """

    def Exception(self):
        """
        The person whose Queen Bee is surrounded loses the game, unless the last piece to surround their Queen Bee also completes the surround of the other Queen Bee. In that case the game is drawn.
        A draw may also be agreed if both players are in a position where they are forced to move the same two pieces over and over again, without any possibility of the stalemate being resolved.
        """
    def __init__(self,board):
        """
        this should describe a hypothetical board state in which above condition is true
        - should this be a board state? or just properties?

        """
        # Idea: modelling conditions as actual board states can be interesting
        #  the goal is to explore rules and to see if there are interesting, but uncommmon strategies
        print(board)
        
        pass

    #def __eq__(self, other): return True
'''
#EndofTheGame = endofTheGame()

class FourthTurn(Rule):
    """
    Your Queen Bee can be placed at any time from your first to your fourth turn.
    You must place your Queen Bee on your fourth turn if you have not placed it before.
    """

class NoClashingColours(Rule):
    """
    pieces may not be placed next to a piece of the opponent's color.
    """




class Game:
    """ the game is made out of interacting parties taking legal actions in sequence """

    colours = 'White', 'Black'

    Pieces = {
        QueenBee: 1,
        Spider: 2,
        Beetle: 2,
        Grasshopper: 3,
        SoldierAnt: 3
    }

    Rules = [
        # rules define valid board configurations and legal actions
        OneHiveRule,
        endofTheGame,
        UnableToMoveOrToPlace,
        FreedomToMove,
        FourthTurn
    ]

    turns = False  # "Hives has turns"
    players = False
    activePlayer = False

    def __init__(self):
        """ GamePlay -The pieces in play define the playing surface, known as the Hive """

        self.Objective = self.ObjectoftheGame  # "surround the enemy Queen"
        self._board = Board(self)
        self._board.setup()



    def Begin(self):
        self.turns = 0
        print('The Game has started')

        print('The first player placing a piece from their hand in the centre of the table')
        self.nextTurn()

        print('The next player joining one of their own pieces to it edge to edge.')
        self.nextTurn()

    def Over(self):
        """ game stops """
        print('this player won! The game ended in {} turns'.format(self.turns))

    def addPlayer(self,player):
        """ enable external input """
        if not self.players: self.players = []
        self.players.append(player)
        print('hi, {}'.format(player))


    def nextTurn(self):
        # check the board state
        if not self._board.VALID:
            # wtf - something has gone wrong
            self.Over()
        else:
            self.turns += 1

    def addPiece(self,piece,player):
        self._board.pieces.append(piece)
        self.nextTurn()

    def ObjectoftheGame(self,Condition):
        """
        The object of the game is to totally surround your opponent's Queen Bee whilst at the same time trying to stop your opponent from doing the same to you.
        The pieces surrounding the Queen Bee can be made up of a mixture of both your pieces and your opponent's.
        The first player to surround their opponent's Queen Bee wins.
        """
        # Achieve condition in which above = True
        ObjectiveFunction = ObjectiveCondition = True
        return ObjectiveFunction

    class Phase:
        """ could be a generator? dunno why but it seems fun """
        # Setup, Turns, End

        def Actions(self):
            # while Turn = yours:
            self.Placing or self.Moving

        def Placing(self,Condition):
            """
            A new piece can be introduced into the game at any time.
            """
            newPiece = self.Pieces[4] # random nr 4
            self._board.pieces.append(newPiece)

        def Moving(self,Condition):
            """
            Once your Queen Bee has been placed (but not before), you can decide whether to use each turn after that to place another tile or to move one of the pieces that have already been placed.
            Each creature has its own way of moving about the Hive and it's possible to move pieces to a position where they touch one or more of your opponent's tiles.
            All pieces must always touch at least one other piece. If a piece the only connection between two parts of the Hive, it may not be moved.
            """
            newPiece = self.Pieces[4]  # random nr 4
            newPiece.doMove()

Hive = Game()
Jack = Jarvis = 'an AI'
Hive.addPlayer(Jarvis)
Hive.addPlayer(Jack)
Hive.Begin()

Hive.addPiece(QueenBee(),Jarvis)


#It is possible to win the game without placing all your pieces but once a piece has been placed it can't be removed.


