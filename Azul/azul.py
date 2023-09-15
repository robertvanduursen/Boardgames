"""

Azul

"""
# UNRESOLVED
# STRATEGY EXTRACTION

'''

exercise in 
- Modelling
- data set generation 

the data set is the model of the game (?)

this yields the ability to explore, test and develop strategies
'''

import enum, random


class Tile(enum.Enum):
    """ the wall tile """
    BLUE = 1
    RED = 2
    YELLOW = 3
    WHITE = 4
    BLACK = 5


class Disc:
    """ the disc """
    tiles = False
    game = False

    def __init__(self):
        self.tiles = []

    def clear(self):
        self.tiles = []
        # move tile to discard
        self.tiles.pop(0)

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remaining_to_marketplace(self):
        """ """
        print('remaining', 'are moved to the market place')
        self.game.marketPlace.tiles += self.tiles
        self.tiles.clear()

    def pick_tiles(self, _type):
        tiles = []
        for idx, _tile in reversed(list(enumerate(self.tiles))):
            if _tile == _type:
                print('pick', _tile, 'at', idx, 'as well')
                tiles.append(self.tiles.pop(idx))
        return tiles

    def pick_tile(self, nr):
        """ remove """
        print('you picked', self.tiles[nr])
        _type = self.tiles[nr]
        tiles = self.pick_tiles(_type)
        self.remaining_to_marketplace()

        return tiles


class MarketPlace(Disc):
    """ the market place """


class TilePouch:
    """ the container """
    tiles = False

    def __init__(self):
        self.tiles = []
        for tile in Tile.__members__:
            # print(tile)
            self.tiles += [tile] * 20

    def shuffle(self):
        """ shuffle the contents of the bag """
        random.shuffle(self.tiles)
        return True

    def get_tile(self):
        """ get a tile out the bag and hand it over """
        return self.tiles.pop(0)


class Board:
    """ the player's board """

    minus_points = [-1, -1, -2, -2, -2, -3, -3]

    points = 0  # modulo 100

    # description of default board - 02/05/2020 19:47
    rows = {
        1: [Tile.BLUE, Tile.YELLOW, Tile.RED, Tile.BLACK, Tile.WHITE],
        2: [Tile.WHITE, Tile.BLUE, Tile.YELLOW, Tile.RED, Tile.BLACK],
        3: [Tile.BLACK, Tile.WHITE, Tile.BLUE, Tile.YELLOW, Tile.RED],
        4: [Tile.RED, Tile.BLACK, Tile.WHITE, Tile.BLUE, Tile.YELLOW],
        5: [Tile.BLUE, Tile.RED, Tile.BLACK, Tile.WHITE, Tile.BLUE],
    }

    slots = {
        1: [None],
        2: [None, None],
        3: [None, None, None],
        4: [None, None, None, None],
        5: [None, None, None, None, None]
    }

    def __init__(self):
        """ """


class Game:
    """ the actual game """
    board = Board
    marketPlace = MarketPlace
    active_player = False
    players = False

    class state(enum.Enum):
        GOING = 0
        OVER = 1

    states = state

    round = 0
    discs = 0
    pouch = TilePouch

    def new_round(self):
        self.pouch.shuffle()

        for disc in self.discs:
            for _ in range(4):
                disc.add_tile(self.pouch.get_tile())

    class Actions:

        def choose_a_tile(self):
            """ on a disc or in the market """
            pass

        def place_a_tile_or_tiles(self):
            pass

        def remainder_become_minus_points(self):
            pass

    def __init__(self):
        self.marketPlace = MarketPlace()
        self.pouch = TilePouch()
        self.discs = [Disc() for _ in range(5)]

        self.players = Player(), AI()
        self.active_player = self.players[0]
        # 2 players
        # 5 discs

        # todo: ugly connection
        for disc in self.discs:
            disc.game = self


    class Round:

        def __init__(self):
            """ structure of a Round """

            '''
            keep going until there are no more tiles to pick
            
            for any player
            for any completed row, place 1 tile on the fresco
            count points that tile makes
            put the rest in the discard place        

            if a fresco has 1 full row, the game is over
            if not, start a new round            
            '''

    def start(self):
        self.new_round()
        self.ask_for_input()

    def ask_for_input(self):
        print('choose your actions -> 1 = pick tile / 2 = see tiles ')
        action = int(input())
        if action == 1:
            print('choose your tile')
            self.list_discs()
            disc = int(input())
            tile = int(input())
            self.active_player.place_down(self.pick_tile(disc, tile))

        else:
            print('see your tiles')
            print(self.active_player.board.slots)

        self.next_turn()

    def next_turn(self):
        if not isinstance(self.active_player, AI):
            self.ask_for_input()

    def list_discs(self):
        for idx, disc in enumerate(self.discs):
            print(idx)
            for idx, tile in enumerate(disc.tiles):
                print('\t', idx, tile)

    def objective(self):
        return 'the most points wins'

    def pick_tile(self, disc, tile):
        # lol; 02/05/2020 20:57 - small short circuit in how to deal with the interactions
        # done: these tiles have to go somewhere
        return self.discs[disc].pick_tile(tile)

    def statistics(self):
        print('the shortest possible game =', 5, 'turns')
        print(5 * 20, 'total tiles')
        print(20, 'each')


class Rules:
    """ check after each turn """
    game = Game

    def game_over(self, game):
        """ if there is one full row; then the round plays out and the game ends """
        if any(len(row.tiles_taken) == 5 for row in self.game.board.rows):
            return Game.states.OVER


    def point_scoring(self):
        """ """



class Player(object):
    board = Board

    def __init__(self):
        self.board = Board()

    def pick_tile(self):
        """ """

        # todo: gets tiles, puts the chosen color on his board
        #  and the remaining on the market place

        # todo: add concept of market place
        # todo: add concept of being able to pick from the marketplace

        return True

    def place_down(self, tiles):
        print('tiles to place', tiles)
        print('choose your row')
        slot = int(input())

        for idx, tile in enumerate(tiles):
            self.board.slots[slot][idx] = tile


class AI(Player):
    """ an AI opponent """


azul = Game()
print(azul.objective())
azul.start()

# 02/05/2020 20:50 done

# resume 02/05/2020 20:50

# 02/05/2020 21:09

# now it has actual game state
# done: it now has actual objects
