from xo import *
from nn import *
from genetic import *

def position(tab):
    i = tab // 3
    j = tab % 3
    return (i, j)

def run(xo, nn1, nn2):
    running = 1
    counter = 0
    while running and counter < 9:
        player  = counter % 2 + 1
        nn = None
        if player == 1:
            nn = nn1
        else:
            nn = nn2
        counter += 1
        if xo.play(player, position(nn.predict(np.reshape(xo.board, (9, 1))))):
            #xo.print()
            return player % 2 + 1, 0
        
        if xo.win() != 0:
            running = 0
            #print(f"Player {player} won")
            #print(xo.board)
            return player, counter
    
    #xo.print()
    #print("No winner")
    return 0, 0

def create_gen(gen_size, shape):
    gen = []
    for _ in range(gen_size):
        gen.append(NN(shape))
    return gen

def run_gen(gen):
    gen_size = len(gen)
    scores = [0 for _ in range(gen_size)]
    xo = XO()
    for i in range(gen_size):
        for j in range(gen_size):
            r, counter = run(xo, gen[i], gen[j])
            if r == 1:
                scores[i] += counter
            elif r == 2:
                scores[j] += counter
            else:
                scores[i] += 1
                scores[j] += 1
            #xo.print()
            xo.reset()
    return scores

def main(nb_gens):
    gen = create_gen(100, (9,3,9))
    for i in range(nb_gens):
        scores = run_gen(gen)
        elites = elitism(gen, scores)
        gen = crossover(elites)
        #print(i, max(scores))

main(500)