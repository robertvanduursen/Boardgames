"""

a Gwent VM

"""


class Stack:
    pass


class VirtualMachine:
    pass


import enum

class instruct(enum.Enum):
    setScoreA = 0x02
    setScoreB = 0x04


test = instruct.setScoreA.value & instruct.setScoreB.value
print(test)