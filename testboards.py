import random
from sys import stdout
import bog
dice = [
    ['a','a','e','e','g','n'],
    ['e','l','r','t','t','y'],
    ['a','o','o','t','t','w'],
    ['a','b','b','j','o','o'],
    ['e','h','r','t','v','w'],
    ['e','h','r','t','v','w'],
    ['c','i','m','o','t','u'],
    ['d','i','s','t','t','y'],
    ['e','i','o','s','s','t'],
    ['d','e','l','r','v','y'],
    ['a','c','h','o','p','s'],
    ['h','i','m','n','qu','u'],
    ['e','e','i','n','s','u'],
    ['e','e','g','h','n','w'],
    ['a','f','f','k','p','s'],
    ['h','l','n','n','r','z'],
    ['d','e','i','l','r','x']
]

cmax = 0
while 1:
    random.shuffle(dice)
    board = []
    for y in range(4):
        row = []
        for x in range(4): row.append(random.choice(dice[4*y+x]))
        board.append(row)
    #board = [['s','t','n','g'],['e','i','a','e'],['d','r','l','s'],['s','e','p','o']]
    b = bog.testboard(board)
    if b>cmax:
        cmax = b
        for y in range(4):
            for x in range(4):
                stdout.write(board[y][x])
            stdout.write('\n')
        stdout.write('\n')
        print b
        print
