import random


def create_individual(n, bounds):
    return [random.uniform(*bounds) for _ in range(n)]


def create_population(pop_size, bounds, n):
    return [create_individual(n, bounds) for _ in range(pop_size)]
