from snk import Snake
from pomme import Pomme
from game import Game
from options import *
from neuralNetwork import creation_de_reseaux, jeu_du_reseau, reseau_de_neurones
from tqdm import tqdm



def run(reseau):
    game = Game()
    val = True
    while val:
        print(game.distpo())
        d = jeu_du_reseau([[game.snkdir()], [game.distpo()[0]], [game.distpo()[1]], [game.blocked()[0]], [game.blocked()[1]], [game.blocked()[2]]], reseau)
        dir = list_dir[(game.snkdir() + d) % 4]
        #   print(d)
        a = game.loop(dir)
        if a == False:
            val = False
        
    
    print(game.snake.body, game.perf())

        #time.sleep(0.2)
    return game.perf()


pop = creation_de_reseaux(100)
run(pop[0])
#for i in range(100):

   # f = run(pop[i])


