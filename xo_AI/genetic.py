def elitism(gen, scores):
    gen_scores = []
    for i in range(len(gen)):
        gen_scores.append((gen[i], scores[i]))
    gen_scores.sort(key = lambda y: y[1], reverse=True)
    #print(gen_scores[:10])

    return [gen_scores[:10][i][0] for i in range(10)]

def crossover(elites):
    children = []
    for i in range(len(elites)):
        children.append(elites[i])
        for j in range(i+1, len(elites)):
            child1, child2 = elites[i].cross(elites[j])
            children.append(child1)
            children.append(child2)
    
    return children