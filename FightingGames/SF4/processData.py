import operator,os,re,sys,inspect # default imports
import xml.etree.cElementTree as ET
from Fighters import *

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(currentPath)

class Move(object):
    def __init__(self):
        super(Move, self).__init__()
        self.MoveName = 'move'
        self.Nickname = '-'
        self.Damage = '-'
        self.Stun = '-'
        self.MeterGain = '-'
        self.HitLevel  = '-'
        self.CancelAbility = '-'
        self.Startup  = '-'
        self.Active  = '-'
        self.Rcvry = '-'
        self.TotalFrames = '-'
        self.AdvOnGuard = '-'
        self.AdvOnHit = '-'
        self.BlockStun = '-'
        self.HitStun = '-'
        self.ExtraDetails = '-'
        self.ArmorBreak = '-'
        self.Proj = '-'
        self.Throw = '-'
        self.OnHitGround = '-'
        self.CounterHitGround = '-'
        self.OnHitAir = '-'
        self.CounterHitAir = '-'
        self.Armor = '-'
        self.FullInvincible = '-'
        self.StrikeInvincible = '-'
        self.ProjectileInvincible = '-'
        self.ThrowInvincible = '-'
        self.Airborne = '-'
        self.JuggleInfo = '-'
tabs =[
'Move Name',
'Nickname',
'Damage',
'Stun',
'Meter Gain',
'Hit Level',
'Cancel Ability',
'Startup',
'Active',
'Rcvry',
'TotalFrames',
'Adv On Guard',
'Adv On Hit',
'Block Stun',
'Hit Stun',
'Extra Details',
'Armor Break',
'Proj',
'Throw',	
'On Hit Ground',
'Counter Hit Ground',
'On Hit Air',
'Counter Hit Air',
'Armor',
'Full Invincible',
'Strike Invincible',	
'Projectile Invincible',
'Throw Invincible',
'Airborne',
'Juggle Info'
]

def processCharData(character):
    folder = currentPath+'/data/'+character
    print(folder)
    if os.path.exists(folder):
        with open(folder+'/frameData.html','rb') as F: data = F.read().replace(b'\r',b' ').replace(b'\n',b' ')
        table = data.split(b'id="Frame_Data">Frame Data<')[1].split(b'id="Notes:">')[0]#.strip()#
        #.split('">')[1:]
        return str(table.split(b'width="2800px">')[1].strip().split(b'</table>')[0].strip())#''.join(table).strip().split('</table>')[0].strip()
    return False

def getMetaData(character,getMetaData):
    folder = currentPath+'/data/'+character
    #print(folder)
    if os.path.exists(folder):
        with open(folder+'/frameData.html','rb') as F: data = F.read().replace(b'\r',b' ').replace(b'\n',b' ')

        table = data.split(b'colspan="6">VITALS')[1].split(b'</table>')[0]
        getMetaData.append(str(table))
        return True
    return False

metaData = {}
for char,parseName in characters.items():
    newChar = Character(char)
    frameData = processCharData(parseName)
    getMetaData(parseName,metaData)
    if frameData:
        #print frameData#[:500]

        blocks = []
        for x in frameData.split('</th></tr>'):
            blocks += x.split('</td></tr>')
        total = 0
        for x in blocks:
            if 'Move Name' in x and 'Startup' in x:
                total += 1
            else:
                pass#
                newMove = Move()
                for idx,y in enumerate(x.split('<td ')[1:]):
                    #print(tabs[idx],'=',y.split('>')[1:][0].split('<')[0].strip())
                    try:
                        exec('newMove.{} = "{}"'.format(tabs[idx].replace(' ',''),y.split('>')[1:][0].split('<')[0].strip()))
                    except: pass
                newChar.Moves.append(newMove)
        print(char,total)

    try:
        folder = currentPath+'/data/'+parseName
        with open(folder+'/frameData.py','w') as F:
            for move in newChar.Moves:
                for x in move.__dict__.items():
                    F.write(str(x).replace('\n',' '))
                    F.write('|')
                F.write('\n')
    except: pass


for x in metaData:
    pass