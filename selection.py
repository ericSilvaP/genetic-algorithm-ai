import random
from fitness_functions import format_decimals


def selection(pop, fitness):
    k = 3
    selected = random.sample(pop, k)
    return min(selected, key=fitness)


def crossover(p1, p2):
    return [
        format_decimals((p1[0] + p2[0]) / 2),
        format_decimals((p1[1] + p2[1]) / 2),
    ]


def mutate(ind, mutation_rate, bounds):
    for i in range(len(ind)):
        if random.random() < mutation_rate:
            ind[i] += random.gauss(0, 0.1)

        ind[i] = format_decimals(max(min(ind[i], bounds[1]), bounds[0]))

    return ind
