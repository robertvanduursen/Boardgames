''' the goal is to become able to play piano '''
import winsound
from PyQt5 import QtGui,QtCore

class Piano:
    w = 0
    b = 1
    start = [w,b]
    keyPattern = [w,w,b,w,b,w,w,b,w,b,w,b]
    end = [w,w]
    fullKeys = start + keyPattern * 7 + end


    mid_C = 'in the middle'
    def __init__(self):
        print('full number of keys',len(self.fullKeys))

        print('white keys',len(['key' for key in self.fullKeys if key == 0]))
        print('black keys',len(['key' for key in self.fullKeys if key == 1]))


if 1 == 0:
    fullKeys = start + [' '] + (keyPattern+[' ']) * 7 + [' '] + end
    print(''.join([str(i) for i in fullKeys]))

class Score:
    ''' the physical medium / recoding of Music '''
    notes = ['C','D','E','F','G','A','B']

    def convertSoundToNotes(self): pass

    def convertNotesToSheet(self): pass

    def convertSheetToSound(self): pass

    def convertSheetToMIDI(self,path):
        print(path)
        png = QtGui.QImage()
        png.load(path,'.png')
        print(png.size())
        stream = QtCore.QDataStream()
        stream << png

    def ScoreToBits(self):
        ''' display similar to guitar hero instead of left-to-right text'''

    class Sheet:
        hor_spacing = 'beat' # i.e. 4-4
        vert_spacing = 'ladder'
        symbols = 'notes'


    
class Musician:
    #Instrument

    class Hand:
    
        class Finger:
            length = 0
            digits = []
            ranges = []

        fingers = [Finger()]*5
        
        def fingerPose(self):
            ''' the pose best suited to ones hand and to produce the note '''
        
    hands = [Hand()]*2

pianist = Musician()
paino = Piano()
sheet = Score()
#sheet.convertSheetToMIDI("D:\Google Drive\Games\score_0.png")


#for x in range(20):    winsound.Beep(308, 2000)