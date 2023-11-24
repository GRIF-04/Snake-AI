import numpy as np
from random import random, randint
from neuralNetwork import creation_de_reseaux
from options import *





def elitism(pop, perf, nb = nb_elites):
    l = []
    for i in range(len(pop)):
        l.append((pop[i], perf[i]))
    l.sort(key = lambda y: y[1], reverse=True)
    res = []
    for k in range(nb):
        res.append(l[k])
    return res




def crossover(elites):
    children = []
    for i in range(len(elites) - 1):
        for j in range(i+1, len(elites)):
            new_gen = {}
            for c in elites[i]:
                new_gen[c] = [[] for o in range(len(elites[i][c]))]
                for k in range(len(elites[i][c])):
                    new_gen[c][k] = [0 for p in range(len(elites[i][c][k]))]
                    for l in range(len(elites[i][c][k])):
                        
                        if random() >= 0.5:
                            new_gen[c][k][l] = elites[i][c][k][l]
                        else:
                            new_gen[c][k][l] = elites[j][c][k][l]
            children.append(new_gen)
    return children



def mutation(children):
    new_children = []
    for gen in children:
        for c in gen:
            for k in range(len(gen[c])):
                for l in range(len(gen[c][k])):
                    r = random()
                    if r >= 0.5:
                        v = randint(-10, 10)
                        var = gen[c][k][l] + (v/100) * gen[c][k][l]
                        
                        if var > 1:
                            gen[c][k][l] = 1
                        elif var < 0:
                            gen[c][k][l] = 0
                        else:
                            gen[c][k][l] = var
                        
        new_children.append(gen)
    return new_children




#elites = creation_de_reseaux(3)
#print(elites, mutation(elites))
#mutation(elites)