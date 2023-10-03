import collections
import numpy as np

sample = [
    1, 0, 0, 0, 0, 0, 0, 0, 6,
    0, 0, 6, 0, 2, 0, 7, 0, 0,
    7, 8, 9, 4, 5, 0, 1, 0, 3,

    0, 0, 0, 8, 0, 7, 0, 0, 4,
    0, 0, 0, 0, 3, 0, 0, 0, 0,
    0, 9, 0, 0, 0, 4, 2, 0, 1,

    3, 1, 2, 9, 7, 0, 0, 4, 0,
    0, 4, 0, 0, 1, 2, 0, 7, 8,
    9, 0, 8, 0, 0, 0, 0, 0, 0,

]


# started 12/02/2020 21:34


class sudokuSolver:
    sudo = np.array
    iterCount = int

    def __init__(self, sudo):
        sudo = np.array(sudo)
        sudo = sudo.reshape((9, 9))

        self.sudo = sudo
        self.iterCount = 1

    def iterate(self):

        si, sy, options, nr = 0, 0, 0, 0  # cell and options
        rowNrs, collNrs = [], []
        trans = np.transpose(self.sudo)

        for idx, (ix, iy) in enumerate(np.ndindex(self.sudo.shape)):
            # print(idx,':',self.sudo[ix, iy])

            row = self.sudo[ix]
            coll = trans[iy]
            # print(row)
            # print(coll)
            # print(idx, ':', ix, iy, '\n')
            # print(self.sudo[ix])
            rowVals = [x for x in row if x != 0]
            collVals = [x for x in coll if x != 0]

            localOptions = len(rowVals) + len(collVals)
            if self.sudo[ix, iy] == 0 and localOptions > options:
                si, sy, = ix, iy
                options = localOptions
                nr = idx
                rowNrs = rowVals
                collNrs = collVals

        print("cell nr {} -> {} @ {},{} with {} set neighbours".format(nr, self.sudo[si, sy], si, sy, options))

        remRows = set(list(range(1, 10))) - set(rowNrs)
        remColls = set(list(range(1, 10))) - set(collNrs)
        candidates = set(remRows) & set(remColls)
        print("candidates: {} of len {}".format(candidates, len(candidates)))

        # print(self.sudo[si])
        # print(trans[sy])
        # print()

        # now examine the actual rows
        if len(candidates) == 1:
            self.sudo[si, sy] = list(candidates)[0]
        else:
            self.sudo[si, sy] = list(candidates)[0]

        print(self.sudo)
        print()

    def sanityCheck(self):
        trans = np.transpose(self.sudo)

        for idx, (ix, iy) in enumerate(np.ndindex(self.sudo.shape)):
            print(idx, ':', self.sudo[ix, iy])

            row = self.sudo[ix]
            checkDict = collections.defaultdict(int)
            for x in row:
                checkDict[x] += 1
            del checkDict[0]
            assert sum(checkDict.values()) == len(checkDict)

            coll = trans[iy]
            checkDict = collections.defaultdict(int)
            for x in coll:
                checkDict[x] += 1
            del checkDict[0]
            assert sum(checkDict.values()) == len(checkDict)

    def solve(self):
        stillZeros = True

        while stillZeros:
            stillZeros = False
            print('iteration {}'.format(self.iterCount))
            for idx, (ix, iy) in enumerate(np.ndindex(self.sudo.shape)):
                if self.sudo[ix, iy] == 0:
                    stillZeros = True
                    break

            self.iterate()
            self.iterCount += 1


# newSudo = sudokuSolver(sample)
# newSudo.solve()


grid = [
    [1, 0, 0, 0, 0, 0, 0, 0, 6, ],
    [0, 0, 6, 0, 2, 0, 7, 0, 0, ],
    [7, 8, 9, 4, 5, 0, 1, 0, 3, ],

    [0, 0, 0, 8, 0, 7, 0, 0, 4, ],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, ],
    [0, 9, 0, 0, 0, 4, 2, 0, 1, ],

    [3, 1, 2, 9, 7, 0, 0, 4, 0, ],
    [0, 4, 0, 0, 1, 2, 0, 7, 8, ],
    [9, 0, 8, 0, 0, 0, 0, 0, 0, ]
]
import copy
oldGrid = copy.deepcopy(grid)

def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for y in range(0, 3):
            if grid[y0 + i][x0 + i] == n:
                return False
    return True





def solve():
    global grid
    global oldGrid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return


    print(np.matrix(oldGrid))
    print()
    print(np.matrix(grid))
    input('More?')


solve()
