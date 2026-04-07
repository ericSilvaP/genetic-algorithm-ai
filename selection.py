import random


def selection(pop, fitness):
    k = 3
    selected = random.sample(pop, k)
    return min(selected, key=fitness)


def crossover(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def mutate(ind, mutation_rate, bounds):
    if random.random() < mutation_rate:
        ind[0] += random.uniform(-0.1, 0.1)
        ind[1] += random.uniform(-0.1, 0.1)

    ind[0] = max(min(ind[0], bounds[1]), bounds[0])
    ind[1] = max(min(ind[1], bounds[1]), bounds[0])

    return ind
