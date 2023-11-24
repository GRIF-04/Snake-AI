from neuralNetwork import res
from genetic import *
from game import Game
from options import *
from neuralNetwork import creation_de_reseaux, run_res_g


def run(reseau):
    game = Game()
    val = True
    tab = []
    while val:
        d = run_res_g([[game.snkdir() / 3], [(game.distpo()[0] +60) / 120], [(game.distpo()[1]+ 20) / 40], [game.blocked()[0]], [game.blocked()[1]], [game.blocked()[2]]], reseau)
        #print(d)
        tab.append(d)
        dir = list_dir[(game.snkdir() + d) % 4]
        a = game.loop(dir)
        if a == False:
            val = False

        #time.sleep(0.2)
    return game.perf()



#print(run(res((6, 8, 4, 3))))


def run_gen(pop):
    perf = []
    for snk in pop:
        perf.append(run(snk))
    return perf


def grif(nb_gen):
    pop = creation_de_reseaux(nb_by_gen, (6, 8, 8, 3))
    perf_t = []
    with open("data.txt", "w") as f:
        for i in range(nb_gen):
            perf = run_gen(pop)
            perf_t.append(perf)
            pop = elitism(pop, perf)
            children = crossover(pop)
            pop.extend(children + mutation(children))
        perf = run_gen(pop)
        f.write(str(elitism(pop, perf)[0]))
    f.close()
    return pop, perf_t


print(grif(50)[1])