from options import *

class Snake():
    

    def __init__(self, l):
        self.x = self.original_x = l[0][1]
        self.y = self.original_y = l[0][0]
        self.body = self.original_body = l

        self.fitness = 300


    def avancer(self, dir):
        if self.fitness == 0:
            return False
        self.fitness -= 1
        new_y = self.y
        new_x = self.x
        if dir == RIGHT:
            new_x += 1
        if dir == LEFT:
            new_x -= 1
        if dir == UP:
            new_y -= 1
        if dir == DOWN:
            new_y += 1
        return (new_y, new_x)


    def maj(self, boo, new_pos):
        self.body.insert(0, new_pos)
        if not boo:
            self.body.pop()
        self.y, self.x = self.body[0]


    def reinitialiser(self):
        self.x = self.original_x
        self.y = self.original_y
        self.body = self.original_body



