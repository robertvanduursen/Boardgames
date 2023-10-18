""" Rubiks Cube Python Solver """


class RubiksCube(object):
    """ RubiPython Class """
    pass

    def constraints(self):
        """ """
        '''
        center of each face = fixed
        you can only rotate
        

        '''

    def options(self):
        """ the moves you can make as a user """
        '''
        swivel a face around its center
        swivel a middle row around its axis (is also a 2x <swivel face around center>
        
        
        '''

    def theory(self):
        """ """
        '''
        a RBC = a Rubiks Cube
        a RBC consists of 29 blocks ((3 * 9) - 1) connected by swivel mechanism in the center of the device
        
        the structure = a cube; a 3D manifold with 6 sides OR faces, each with its own colour
        so, 6 colours total

        a State = 1 empty space on a theoretical cube that can be occupied by an actual block
        
        
        every corner can occupy 1 of 8 states
        9 x 6 = 54 squares
        6 x 1 = 6 centres
        (4 * 6 ) / 2 = 12 (cardinal) duo's
        
        (4 * 6) / 3 = 8 (triples) corners
        each corner is a unique combination of 3 colours (triplet)

        '''

    def questions(self):
        """ """
        '''

        how many configurations can a RBC have?
        1 of 208 configs = <Solved>

        '''

    def assertions(self):
        """ """
        '''
        assert = 1 valid solution
        assert implies that there are no partial solutions -> i.e. 1 face solved is not enough / done
        
        
        assert property = mathematically, the RBC is a convergent series
        
        
        this implies that a move can put the RBC closer or further from solved
        this implies Distance -> there are right & wrong moves, if goal of move = closer to solved


        '''

    def translation(self):
        """ into mathematics """
        '''
        a unfoldable (2D) manifold with <shift 3> operations
        a twist in 3D == a shift 3 in 2-sphere

        entropy = [
            1 = fully scrambled
            0 = fully solved 
        ]

        '''

    def langauge(self):
        """ lexicon """
        '''
        
        configuration = 'permutation'  # -> perm

        assertion = 'every configuration is solvable in 20 moves or less'
        implication = 'each correct move reduces entropy ?'
        
        
        hypothesis = 'from any random config; is there only 1 valid path back to <Solved> ?'

        
        '''

class Solver:
    pass

# 03/07/2020 12:18


'''


full solved RBC = max aligned


03/07/2020 12:46
Action = go from axiom to derived / emerged

'''
