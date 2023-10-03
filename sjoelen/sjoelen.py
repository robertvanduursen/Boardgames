''' modelling of the traditional Dutch game Sjoelen '''
# default unit = cemtimeter; to keep it int-based

class Stone:
    material = 'Wood'  # physical properties
    radius = 5  # cm
    inertia = 0
    x, y = 0, 0

    def isTravelling(self):
        """ attempt to model physics and movement """
        # update pos
        pass

    def onImpact(self):
        """ the transfer of forces - the book-keeping """
        pass


class Board:
    length = 111  # cm; = runway
    width = 38  # cm

    runway =     44 # cm; the area on which the player can prepare its slide
    slotWidth =  6 #cm
    slotIndent = 2 # cm
    laneLength = 36  # cm
    laneWidth =  9  # cm

    slots = {
        2: [],
        3: [],
        4: [],
        1: []
    }

    # phys prop
    friction = 9

    def __init__(self):
        self.stones = [] # empty board

    @property
    def maxStonesInLane(self):
        return int(self.laneLength / Stone.radius)

    def prevState(self):
        ''' a way to resolve kinematics'''
        '''
        old state + new stone -> needs update
        the updateStep wil dictate smoothness
        
        this old state = effectively the starting state 
        '''
        pass

    def waitTillStoneSettled(self):
        ''' while there is still energy in the board '''
        pass
       
       
   
class Game:
    stones = [Stone()]*30
    board = Board()
    score = 0
    
    def __init__(self):
        self.board.slots[3].append(1)

    def allSlotsRule(self):
        # bonus points
        if all(stones for stones in self.board.slots.values()):
            return 10
        return 10
            
    def getScore(self):
        print(self.score)
        
    def bestDistri(self):
        print('maxStonesInLane',self.board.maxStonesInLane) # this doesnt account for zig zag

        return self.nrStones*max(self.board.slots.keys())
        
    def maxScore(self):
        # relies on hypo board state
        total = self.allSlotsRule() + self.bestDistri()
        print(total)
    
    @property
    def nrStones(self):
        return len(self.stones)
        

        
    def stats(self):
       print('nr stones',self.nrStones)
       print('nr slots',len(self.board.slots))
       
    def boardState(self):
        ''' state at rest '''
        pass
    
    def slideStone(self):
        ''' the only action a player can do '''
        # todo: has to factor in direction, speed
        self.stones.pop()
        newStone = Stone()
        newStone.dir = (1.2,3.4)
        newStone.mag = 2.1
        self.board.stones.append(newStone)
        
        self.board.waitTillStoneSettled()
    
    def update(self):
        ''' the board resolves its own state '''
        self.slideStone()
        pass

    def bestSequence(self):
        ''' more based on probability & skill '''
        # todo: this is also
        return [1]*self.nrStones

    def bestStrategy(self):
        ''' more based on probability & skill '''

        #todo: this is the question we are trying to answer!

        return bestSequence + bestSS






sjoelen = Game()
print(sjoelen.bestDistri())
