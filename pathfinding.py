#!/usr/bin/python

import math

symbol = { -1: "x", 0: "<", 1: ">", 2: "^", 3: "v" }
move = { '<': 0, '>': 1, '^': 2, 'v': 3 }
patterns = {
    "x":        '',
    "<>":       'x',
    "><":       'x',
    ">^<v":     'x',
    "^v":       'x',
    "v^":       'x',
    "<^>v":     'x'
}

def optimize(moves, rec = 0):
    """
    Recursive function that returns the final move array
    """
    s = "".join([symbol[i] for i in moves])    

    for i in patterns:
        if s.count(i) != 0: rec = 1
        s = s.replace(i, patterns[i])
    s = s.replace('x', '')
   
    if rec == -1: return [move[i] for i in s]
    if rec == 1: return optimize([move[i] for i in s], 0)
    return optimize([move[i] for i in s], -1)

class Vec2i:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

    def __eq__(self, a):
        return self.x == a.x and self.y == a.y

class Player(Vec2i):
    def __init__(self, x, y, lab = []):
        Vec2i.__init__(self, x, y)
        self.labyrinth = lab

    def length(self, b):
        return math.sqrt((b.x-self.x)**2 + (b.y-self.y)**2)

    def canMove(self, o, nope):
        """
        Checks  if the player can move
        """
        to_go = Vec2i(0,0)
        if o == 1: to_go = Vec2i(self.x+1, self.y)
        elif o == 0: to_go = Vec2i(self.x-1, self.y)
        elif o == 2: to_go = Vec2i(self.x, self.y-1)
        elif o == 3: to_go = Vec2i(self.x, self.y+1)

        if self.labyrinth[to_go.y][to_go.x] != '#' and [to_go.x, to_go.y] not in nope:
            return True
        else:
            return False

    def best_way(self, b, size, nope, last = -1):
        """
        Checks the best way to go
        """

        leng = []

        if (last != 1 and 0 < self.x and 
            self.canMove(0, nope)):
            leng.append( [Player(self.x-1, self.y).length(b), 0] )
        if (last != 3 and 0 < self.y and 
            self.canMove(2, nope)):
            leng.append( [Player(self.x, self.y-1).length(b), 2] )
        if (last != 0 and self.x < size.x and 
            self.canMove(1, nope)):
            leng.append( [Player(self.x+1, self.y).length(b), 1] )
        if (last != 2 and self.y < size.y and 
            self.canMove(3, nope)):
            leng.append( [Player(self.x, self.y+1).length(b), 3] )

        if len(leng) == 1:
            if [self.x, self.y] not in nope: nope.append([self.x, self.y])
            return leng[0][1]
        elif len(leng) == 0: 
            if [self.x, self.y] not in nope: nope.append([self.x, self.y])
            try:
                return self.best_way(b, size, [], last)
            except RuntimeError:
                return -1

        lengt = [i[0] for i in leng] 

        m = max(lengt)

        best = [m,-1]
        for i in leng:
            if i[0] <= best[0]:
                best = i

        return best[1]

    def move_to(self, o):
        """
        Moves the player
        """
        if o == 0:
            self.x -= 1
        elif o == 1:
            self.x += 1
        elif o == 2:
            self.y -= 1
        elif o == 3:
            self.y += 1

    def move_player(self, moves):
        """
        Move it from a 'move' array
        """
        for i in moves:
            self.move_to(i)
            print(symbol[i], end="")
        print()

    def print_lab(self):
        """
        Re-prints the labyrinth
        """
        final = []
        for y, line in enumerate(self.labyrinth):
            final.append("")
            for x, char in enumerate(line): 
                if self == Vec2i(x, y):
                    final[y] += 'o'
                elif char == ' ' or char == 'o':
                    final[y] += ' '
                elif char == 'S':
                    final[y] += 'S'    
                elif char == '#':
                    final[y] += '#'

        print("\n".join(final))       

    def getMoves(self, destination, size):
        """
        Solves it, optimizes it, prints it
        """
        x, y = (self.x, self.y)

        moves = []
        nope = []

        o = -1
        while self != destination and o != -2:
            o = self.best_way(destination, size, nope, o)
            self.move_to(o)
            if o != -2: moves.append(o)

        moves = optimize(moves)
        Player(x, y).move_player(moves)

def solve(labyrinth):
    """
    Solves the labyrinth
    """
    labyrinth = labyrinth.rstrip("\n").split("\n")

    destination = Vec2i(0,0)
    player = Player(0,0, labyrinth)

    size = [0,0]
    for y, line in enumerate(labyrinth):
        size[0] += 1
        for x, char in enumerate(line):
            size[1] += 1
            if char == 'o':
                player.x, player.y = (x, y)
            elif char == 'S':
                destination = Vec2i(x, y)

    size = Vec2i(size[1], size[0])
    player.getMoves(destination, size)

"""
labyrinth = "\
########S##\n\
#         #\n\
##### #####\n\
#o        #\n\
###########"
"""

labyrinth = "\
##################\n\
#S          ######\n\
###########  #####\n\
#o   ##  ### ##  #\n\
###  ## #### ### #\n\
###              #\n\
##################"

solve(labyrinth)
