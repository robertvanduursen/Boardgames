'''
a few exception cases for handling internet scrapping
'''
import os
import json

characters ={
    'Kyo' : "/The_King_of_Fighters_XIII/Kyo",
    'Benimaru' : "/The_King_of_Fighters_XIII/Benimaru",
    'Daimon' : "/The_King_of_Fighters_XIII/Daimon",
    'Terry' : "/The_King_of_Fighters_XIII/Terry",
    'Andy' : "/The_King_of_Fighters_XIII/Andy",
    'Joe' : "/The_King_of_Fighters_XIII/Joe",
    'Billy' : "/The_King_of_Fighters_XIII/Billy",
    'Ash' : "/The_King_of_Fighters_XIII/Ash",
    'Saiki' : "/The_King_of_Fighters_XIII/Saiki",
    'EX Iori' : "/The_King_of_Fighters_XIII/EX_Iori",
    'EX Kyo' : "/The_King_of_Fighters_XIII/EX_Kyo",
    'Mr. Karate' : "/The_King_of_Fighters_XIII/Mr._Karate",
    'Ryo' : "/The_King_of_Fighters_XIII/Ryo",
    'Robert' : "/The_King_of_Fighters_XIII/Robert",
    'Takuma' : "/The_King_of_Fighters_XIII/Takuma",
    'Iori' : "/The_King_of_Fighters_XIII/Iori",
    'Mature' : "/The_King_of_Fighters_XIII/Mature",
    'Vice' : "/The_King_of_Fighters_XIII/Vice",
    'Saiki (Boss)' : "/The_King_of_Fighters_XIII/Saiki_(Boss)",
    'Elisabeth' : "/The_King_of_Fighters_XIII/Elisabeth",
    'Duo Lon' : "/The_King_of_Fighters_XIII/Duo_Lon",
    'Shen' : "/The_King_of_Fighters_XIII/Shen",
    'Kim' : "/The_King_of_Fighters_XIII/Kim",
    'Hwa Jai' : "/The_King_of_Fighters_XIII/Hwa_Jai",
    'Raiden' : "/The_King_of_Fighters_XIII/Raiden",
    'Mai' : "/The_King_of_Fighters_XIII/Mai",
    'King' : "/The_King_of_Fighters_XIII/King",
    'Yuri' : "/The_King_of_Fighters_XIII/Yuri",
    'K' : "/The_King_of_Fighters_XIII/K%27",
    'Kula' : "/The_King_of_Fighters_XIII/Kula",
    'Maxima' : "/The_King_of_Fighters_XIII/Maxima",
    'Athena' : "/The_King_of_Fighters_XIII/Athena",
    'Kensou' : "/The_King_of_Fighters_XIII/Kensou",
    'Chin' : "/The_King_of_Fighters_XIII/Chin",
    'Ralf' : "/The_King_of_Fighters_XIII/Ralf",
    'Clark' : "/The_King_of_Fighters_XIII/Clark",
    'Leona' : "/The_King_of_Fighters_XIII/Leona",
    'Dark Ash' : "/The_King_of_Fighters_XIII/Dark_Ash",
 }



def translate(tag):
    transDict = {
        'H':'High',
        'L': 'Low',
        'HL': 'High & Low',
        'su': 'super',
        'sp/su': 'super and somehting',
        'X': 'Yes',

    }
    if tag in transDict.keys():
        return transDict[tag]
    else:
        return tag


class Move:
    """ basic framework on a move in KoF 13 """
    holder = False # dummy

    Name = False
    Startup = False
    Active = False
    Recovery = False
    Hit_Adv = False
    Block_Adv = False

    info = False
    extension = False

    test1 = False
    test2 = False




    def __init__(self):
        # print([lol for lol in dir(self) if not lol.startswith('_')])
        pass

    def attrOrder(self):
        # ['', '↓↙←,←↙↓↘→AC(Air)', 7.0, '-', 'Landing+16', 'Knockdown', '-', '', 'Freeze of 29', '', '']
        return ['holder', 'Name',  'Startup', 'Active', 'Recovery',  'Hit_Adv', 'Block_Adv',  'info',  'extension','test1', 'test2']


    # def parseDamage(self):
    #     self.DamageCalc = self.Damage  # store for later ref
    #     if type(self.Damage) != type(bool()) and type(self.Damage) != type(int()):
    #         #print('\n',self.MoveName, type(self.Damage), self.Damage)
    #         self.DamageCalc = self.Damage # store for later ref
    #         try:
    #             calc = self.Damage
    #             calc = calc.replace('x','*')
    #             self.Damage = eval(calc)
    #         except Exception:
    #             self.Damage = -1
    #
    #     #if self.MoveName == '': self.MoveName = self.Nickname+'_(NickName)'
    #     if not self.MoveName: self.MoveName = str(self.Nickname) + '_(NickName)'

    @property
    def totalSpeed(self):
        speed = 0
        if type(self.Startup) != type(''): speed += self.Startup
        if type(self.Active) != type(''): speed += self.Active
        if type(self.Recovery) != type(''): speed += self.Recovery

        return speed


class Character(object):
    def __init__(self, name):
        super(Character, self).__init__()
        self.name = name
        self.Moves = []

    def printAllStats(self):
        for idx, move in enumerate(sorted(self.Moves, key=lambda x: x.Damage, reverse=True)):
            superString = ''
            printOrder = [
                ('MoveName',35),
                ('Nickname',25),
                ('Damage',10),
                ('DamageCalc', 17),
                ('Stun',10),
                ('MeterGain',20),
                ('HitLevel',20),
                ('CancelAbility',20),
                ('Startup',20),
                ('Active',30),
                ('Rcvry',20),
                ('TotalFrames',20),
                ('AdvOnGuard',20),
                ('AdvOnHit',20),
                ('BlockStun',20),
                ('HitStun',20),
                ('ArmorBreak',20),
                ('Proj',20),
                ('Throw',20),
                ('OnHitAir',20),
                ('CounterHitAir',20),
                ('Armor',20),
                ('FullInvincible',20),
                ('StrikeInvincible',20),
                ('ProjectileInvincible',20),
                ('ThrowInvincible',20),
                ('Airborne',20),
                ('JuggleInfo',60),
                ('DamageCalc',20),
                ('OnHitGround', 56),
                ('CounterHitGround', 56),
                ('ExtraDetails', 30)
            ]
            for item,offset in printOrder:
                val = move.__dict__[item]
                if val == False: val = '~'
                superString += str(item)+': '+str(val)+' '*(offset-len(str(val)))
            print(idx,' '*(2-len(str(idx))),superString)

    def load(self,parseName=False):
        root = os.path.dirname(__file__)
        frameData = json.load(open(os.path.join(root, 'data/%s.json' % self.name)))

        for data in frameData:
            move = Move()
            for attr, val in data.items():
                if isinstance(val,str) and val.isdigit():
                    data[attr] = eval(val)
            move.__dict__ = data
            self.Moves.append(move)

    def getMeMax(self,attr):
        moveList = [(move.Name,eval('move.{}'.format(attr))) for move in self.Moves]
        localMax = sorted(moveList,key= lambda x:-x[1])[0]
        return localMax


    def style(self):
        """ movement style, damage style """


Fighter = Character
