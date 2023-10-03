'''
a few exception cases for handling internet scrapping
'''
import os
characters ={
    'Abel':'Abel',
    'Adon':'Adon',
    'Akuma':'Akuma',
    'Balrog':'Balrog',
    'Blanka':'Blanka',
    'C. Viper':'C._Viper',
    'Cammy':'Cammy',
    'Chun-Li':'Chun-Li',
    'Cody':'Cody',
    'Dan':'Dan',
    'Decapre':'Decapre',
    'Dee Jay':'Deejay',
    'Dhalsim':'Dhalsim',
    'Dudley':'Dudley',
    'E. Honda':'E._Honda',
    'El Fuerte':'El_Fuerte',
    'Elena':'Elena',
    'Evil Ryu':'Evil_Ryu',
    'Fei Long':'Fei_Long',
    'Gen':'Gen',
    'Gouken':'Gouken',
    'Guile':'Guile',
    'Guy':'Guy',
    'Hakan':'Hakan',
    'Hugo':'Hugo',
    'Ibuki':'Ibuki',
    'Juri':'Juri',
    'Ken':'Ken',
    'M. Bison':'M._Bison',
    'Makoto':'Makoto',
    'Oni':'Oni',
    'Poison':'Poison',
    'Rolento':'Rolento',
    'Rose':'Rose',
    'Rufus':'Rufus',
    'Ryu':'Ryu',
    'Sagat':'Sagat',
    'Sakura':'Sakura',
    'Seth':'Seth',
    'T. Hawk':'T._Hawk',
    'Vega':'Vega',
    'Yang':'Yang',
    'Yun':'Yun',
    'Zangief':'Zangief',
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

    def activate(self):
        for item,val in self.__dict__.items():
            #if item == 'Damage': print(item,val)
            if val.isdigit():
                exec('self.{} = {}'.format(item,val))
            if val == '-':
                exec('self.{} = False'.format(item))

    def translateTags(self):
        for item, val in self.__dict__.items():
            if type(val) == type(''):
                if val == '':
                    exec('self.{} = False'.format(item))
                else:
                    val = translate(val)
                    exec('self.{} = "{}"'.format(item, val))


    def parseDamage(self):
        self.DamageCalc = self.Damage  # store for later ref
        if type(self.Damage) != type(bool()) and type(self.Damage) != type(int()):
            #print('\n',self.MoveName, type(self.Damage), self.Damage)
            self.DamageCalc = self.Damage # store for later ref
            try:
                calc = self.Damage
                calc = calc.replace('x','*')
                self.Damage = eval(calc)
            except Exception:
                self.Damage = -1

        #if self.MoveName == '': self.MoveName = self.Nickname+'_(NickName)'
        if not self.MoveName: self.MoveName = str(self.Nickname) + '_(NickName)'

    @property
    def totalSpeed(self):
        speed = 0
        if type(self.Startup) != type(''): speed += self.Startup
        if type(self.Active) != type(''): speed += self.Active
        if type(self.Rcvry) != type(''): speed += self.Rcvry

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
        parseName = characters[self.name]

        root = os.path.dirname(__file__)
        with open(os.path.join(root,r"data\{}\frameData.py".format(parseName)),'r') as F:
            frameData = F.readlines()
        for data in frameData:
            stats = [eval(f) for f in data.split('|')[:-1]]
            move = Move()
            move.__dict__ = {key: val for key, val in stats}
            move.activate()
            move.translateTags()
            move.parseDamage()
            self.Moves.append(move)

    def getMeMax(self,attr):
        moveList = [(move.MoveName,eval('move.{}'.format(attr))) for move in self.Moves]
        localMax = sorted(moveList,key= lambda x:-x[1])[0]
        return localMax

    def getVitals(self,output=False):
        import re

        parseName = characters[self.name]

        root = os.path.dirname(__file__)
        with open(os.path.join(root,r"data\{}\frameData.html".format(parseName)),'rb') as FH:
            data = FH.read()  # .replace(b'\n',b'_')
        vitals = re.search(b'VITALS(.*\S*)?</table>', data, re.S)[0]
        # print(d)

        returnDict = {}

        parameters = [
            "Health",
            "Stun",
            "W-Ultra Scaling",
            "Forward Walk Speed",
            "Forward Dash Distance",
            "Back Walk Speed",
            "Forward Dash Total Frames",
            "Back Dash Distance",
            "Jump Height Apex",
            "Back Dash Total Frames",
            "Jump Total Frames",
            "Back Dash Invincibility",
            "Forward Jump Distance",
            "Back Dash Airborne",
            "Back Jump Distance",
            "Back Dash Recovery",
            # THROWS
            "Forward Throw Range",
            "Back Throw Range",
            #	WAKE-UP TIMING
            "Face Up Total Frames",
            "Face Down Total Frames",
            # ""
            # "High Attacks:	Sekku
            # "Hard Knockdowns:	Crouch HK
            # "Low Attacks:	Crouch LK, Crouch MK, Crouch HK
            # "Armor Breakers:	Shikusen, EX Shikusen, Kaisen Dankairaku
            # ""
            "Level 1 Focus Startup Frames",
            "Level 2 Focus Startup Frames",
            "Level 3 Focus Startup Frames",
            "L1 Focus Attack Forward Dash",
            "L2 FA Forward Dash (On Block)",
            "L1 Focus Attack Back Dash",
            "L2 FA Back Dash (On Block)",
        ]

        for x in parameters:
            byteName = eval('b"%s"' % x.replace('(', '\(').replace(')', '\)'))
            # print(byteName)
            result = re.compile(byteName + b"(.|\s)*?</td>")
            val = re.findall(b'>([\d\.]+)', result.search(vitals)[0])
            if val:
                val = val[0]
            else:
                pass  # print('cant handle',x)
                val = str(val)

            codeName = x.replace('-', '_').replace(' ', '_').replace(')', '_').replace('(', '_')
            exec(r'%s = val' % (codeName))

            locs = dict(locals())
            val = eval(locs[codeName])
            if output: print(x, ' ' * (20 - len(codeName)), val )
            returnDict[x] = val
        # if d: print(d.groups())
        # getMetaData
        return returnDict

    def style(self):
        """ movement style, damage style """


Fighter = Character


