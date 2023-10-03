import xlrd, json, os



wb = xlrd.open_workbook(r"C:\Users\rober\Google Drive\Games\FightingGames\KoF13\data\KoF XIII Frame Data by Atma @KM_Atma.xls")
sheet = wb.sheet_by_index(1)
print(len(wb.sheets()))
sheet.cell_value(0, 0)


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




def moveBlock(sheet):
    i = 0
    for i in range(3, sheet.nrows - 3):
        if "['', 'Move', 'Startup'" in str(sheet.row_values(i)):
            break
    return (3, i-1)


def getMoves(sheet):
    start, end = moveBlock(sheet)
    moves = []
    for i in range(start, end):
        if "['DM', " not in str(sheet.row_values(i)):
            if "['SDM/NeoMAX', " not in str(sheet.row_values(i)):
                # print(sheet.row_values(i))

                newMove = Move()
                for attr, value in zip(newMove.attrOrder(),sheet.row_values(i)):
                    newMove.__dict__[attr] = value

                moves.append(newMove.__dict__)

    return moves

def allInfo():
    info = ''

    for nr in range(1,len(wb.sheets())-1):
        sheet = wb.sheet_by_index(nr)
        print(sheet.cell_value(0, 0), sheet.nrows, 'x', sheet.ncols)


        for i in range(sheet.nrows):
            info += str(sheet.row_values(i))

    return info
#
# data = allInfo()
# print(data.count('Blockstun'))


def MovesToJson():

    root = os.path.dirname(__file__)
    for nr in range(1,len(wb.sheets())-1):
        sheet = wb.sheet_by_index(nr)
        name = sheet.cell_value(0, 0)
        print(name , sheet.nrows, 'x', sheet.ncols)

        moves = getMoves(sheet)

        print('moves', len(moves))
        print()

        with open(os.path.join(root, 'data/%s.json' % name), 'w') as newFile:
            json.dump(moves, newFile)




MovesToJson()