'''
the commonalities across every fighting game
'''

class Game:
    roster = False

    class Character(object):
        moves = False
        def __init__(self, name):
            super().__init__()
            self.name = name


        class Move:
            name = False
            def __init__(self): pass

    class Mechanics:
        type = False


class Move(object):
    def __init__(self):
        super(Move, self).__init__()
        self.MoveName = 'move'
        self.Nickname = False
        self.Damage = False
        self.Stun = False
        self.MeterGain = False
        self.HitLevel  = False
        self.CancelAbility = False
        self.Startup  = False
        self.Active  = False
        self.Rcvry = False
        self.TotalFrames = False
        self.AdvOnGuard = False
        self.AdvOnHit = False
        self.BlockStun = False
        self.HitStun = False
        self.ExtraDetails = False
        self.ArmorBreak = False
        self.Proj = False
        self.Throw = False
        self.OnHitGround = False
        self.CounterHitGround = False
        self.OnHitAir = False
        self.CounterHitAir = False
        self.Armor = False
        self.FullInvincible = False
        self.StrikeInvincible = False
        self.ProjectileInvincible = False
        self.ThrowInvincible = False
        self.Airborne = False
        self.JuggleInfo = False
        self.DamageCalc = False

        self.MovementPattern = 'intersting'


    def movePattern(self):
        """ a way to encode the way the move plays out upon execution """

        # needs Vector 2 coordinates to describe an curve



