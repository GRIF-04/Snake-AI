from options import *
from random import randint


class Pomme():

    def __init__(self,tu):
        self.tu = tu


    def renait(self):
        self.tu = (randint(y_min + 1, y_max - 1), randint(x_min + 1, x_max - 1))