from genetic import *
from snk import Snake
from pomme import Pomme
from game import Game
from options import *
from neuralNetwork import creation_de_reseaux, jeu_du_reseau, run_res_g
import numpy as np
from tqdm import tqdm


def run(reseau):
    game = Game()
    val = True
    tab = []
    while val:
        d = run_res_g([[game.snkdir()], [game.distpo()[0]], [game.distpo()[1]], [game.blocked()[0]], [game.blocked()[1]], [game.blocked()[2]], [len(game.snake.body)]], reseau)
        tab.append(d)
        dir = list_dir[(game.snkdir() + d) % 4]
        a = game.loop(dir)
        if a == False:
            val = False

        #time.sleep(0.2)
    return game.perf()






def run_gen(pop):
    perf = []
    for snk in pop:
        perf.append(run(snk))
    return perf


def grif(nb_gen):
    pop = creation_de_reseaux(nb_by_gen, (7, 8, 8, 8, 3))
    perf_t = []
    with open("data.txt", "w") as f:
        for i in tqdm(range(nb_gen)):
            perf = run_gen(pop)
            perf_t.extend(perf)
            pop = elitism(pop, perf)
            #print(elites)
            children = crossover(pop)
            pop.extend(children + mutation(children))
    f.close()
    return pop, perf_t

print(grif(500)[1])
