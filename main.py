from random import *

class player:
    def __init__(self, name, color=0):
        self.name = name
        self.color = color

    def width(self, b):
        for i in range(len(b)):
            for j in range(len(b[i])-4):
                if b[i][j] == b[i][j+1] == b[i][j+2] == b[i][j+3] == b[i][j+4] == self.color:
                    return True
    def height(self, b):
        for i in range(len(b[0])):
            for j in range(len(b)-4):
                if b[j][i] == b[j+1][i] == b[j+2][i] == b[j+3][i] == b[j+4][i] == self.color:
                    return True
    def diagonal(self, b):
        for i in range(len(b)-4):
            for j in range(len(b[i])-4):
                if b[i][j] == b[i+1][j+1] == b[i+2][j+2] == b[i+3][j+3] == b[i+4][j+4] == self.color:
                    return True

    def check(self, b):
        w = self.width(b)
        h = self.height(b)
        d = self.diagonal(b)
        if w or h or d:
            return True

a = []
line = []
for i in range(19):
    line.append(0)
for i in range(19):
    a.append(line)

p1 = player('p1', 1)
p2 = player('p2', 2)
turn = randint(0, 1)

while True:
    for i in range(len(a)):
        print(a[i])
    
    if turn == 0:
        print('p1 turn')
        x = int(input('x: ')) - 1
        y = int(input('y: ')) - 1
        if a[y][x] == 0:
            a[y][x] = 1
            turn = 1
        else:
            print('wrong')
            continue
    else:
        print('p2 turn')
        x = int(input('x: ')) - 1
        y = int(input('y: ')) - 1
        if a[y][x] == 0:
            a[y][x] = 2
            turn = 0
        else:
            print('wrong')
            continue

    if p1.check(a):
        print('p1 WIN')
        break
    elif p2.check(a):
        print('p2 WIN')
        break
