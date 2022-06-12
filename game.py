from options import *
from random import randint
from snk import Snake
from pomme import Pomme
from neuralNetwork import reseau_de_neurones


class Game():


    def __init__(self):
        self.snake = Snake([(4, 10), (4, 9), (4, 8)])
        self.pomme = Pomme((randint(y_min + 1, y_max - 1), randint(x_min + 1, x_max - 1)))
        #self.reseau = reseau
        self.score = 0

    
    def avancer(self, dir):
        if dir == RIGHT:
            if (self.snake.x + 1) < (x_max - 1) :
                new_pos = self.snake.avancer(dir)
            else: return False
        if dir == LEFT:
            if (self.snake.x - 1) > (x_min + 1) :
                new_pos = self.snake.avancer(dir)
            else: return False
        if dir == UP:
            if (self.snake.y - 1) > (y_min + 1) :
                new_pos = self.snake.avancer(dir)
            else: return False
        if dir == DOWN:
            if (self.snake.y + 1) < (y_max - 1) :
                new_pos = self.snake.avancer(dir)
            else: return False
        return new_pos
    

    def snkdir(self):
        dx = self.snake.x - self.snake.body[1][1]
        dy = self.snake.y - self.snake.body[1][0]
        if dx == 1:
            return 2
        if dx == -1:
            return 0
        if dy == 1:
            return 3
        if dy == -1:
            return 1
    

    def distpo(self):
        dx = self.pomme.tu[1] - self.snake.x
        dy = self.pomme.tu[0] - self.snake.y
        return (dx, dy)
    

    def perf(self):
        return 100 * self.score - self.snake.fitness
    
    def blocked(self):
        dir = self.snkdir()
        b = [0, 0, 0]
        if dir == 0:
            if self.snake.x - 1 <= 0 or (self.snake.y, self.snake.x - 1) in self.snake.body:
                b[1] = 1
            if self.snake.y - 1 <= 0 or (self.snake.y - 1, self.snake.x) in self.snake.body:
                b[2] = 1
            if self.snake.y + 1 >= y_max or (self.snake.y + 1, self.snake.x) in self.snake.body:
                b[0] = 1
        
        if dir == 1:
            if self.snake.y - 1 <= 0 or (self.snake.y - 1, self.snake.x ) in self.snake.body:
                b[1] = 1
            if self.snake.x - 1 <= 0 or (self.snake.y, self.snake.x - 1) in self.snake.body:
                b[0] = 1
            if self.snake.x + 1 >= x_max or (self.snake.y, self.snake.x + 1) in self.snake.body:
                b[2] = 1

        if dir == 2:
            if self.snake.x + 1 >= x_max or (self.snake.y, self.snake.x + 1) in self.snake.body:
                b[1] = 1
            if self.snake.y - 1 <= 0 or (self.snake.y - 1, self.snake.x) in self.snake.body:
                b[0] = 1
            if self.snake.y + 1 >= y_max or (self.snake.y + 1, self.snake.x) in self.snake.body:
                b[2] = 1
        
        if dir == 3:
            if self.snake.y + 1 >= y_max or (self.snake.y + 1, self.snake.x) in self.snake.body:
                b[1] = 1
            if self.snake.x - 1 <= 0 or (self.snake.y, self.snake.x - 1) in self.snake.body:
                b[2] = 1
            if self.snake.x + 1 >= x_max or (self.snake.y, self.snake.x + 1) in self.snake.body:
                b[0] = 1
        return b
            



    def reinit(self):
        self.snake.reinitialiser()
        self.pomme.renait()
        self.score = 0
    

    def loop(self, dir):
        if dir == 'ESC':
            return False
        
        new_pos = self.avancer(dir)

        if new_pos == False:
            return False

        
        if new_pos == self.pomme.tu:
            if self.snake.fitness + 150 > 600:
                self.snake.fitness = 600
            else:
                self.snake.fitness += 150
            self.score += 1
            self.pomme.tu = ()
            while self.pomme.tu == ():
                self.pomme.renait()
                if self.pomme.tu in self.snake.body[1:]:
                    self.pomme = ()
            self.snake.maj(True, new_pos)
        else:
            self.snake.maj(False, new_pos)
        
