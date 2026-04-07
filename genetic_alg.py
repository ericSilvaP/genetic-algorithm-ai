from config_type import Individual
from metrics import Metrics
from create_population import create_population
from selection import selection, crossover, mutate


def genetic_algorithm(pop_size, generations, config, mutation_rate, stop_count):
    metrics = Metrics()
    population = create_population(pop_size, config.bounds, config.n)
    fitness = config.func

    best_fitness = float("inf")
    stagnation_count = 0

    for _ in range(generations):
        population = [
            Individual(ind, metrics.evaluate(ind, fitness)) for ind in population
        ]
        best_ind = min(population, key=lambda ind: ind.fitness)
        best_gen_fitness = best_ind.fitness

        if best_gen_fitness < best_fitness:
            best_fitness = best_gen_fitness
            stagnation_count = 0
        else:
            stagnation_count += 1

        if stagnation_count >= stop_count:
            break

        new_population = []

        for _ in range(pop_size):
            p1 = selection(population, lambda ind: ind.fitness).genes
            p2 = selection(population, lambda ind: ind.fitness).genes

            child = crossover(p1, p2)

            if mutation_rate:
                child = mutate(child, mutation_rate, config.bounds)

            new_population.append(child)

        population = new_population

    return best_fitness, metrics.nfe


def success_rate(
    config, pop_size, generations, stop_count, runs=100, mutation_rate=None
):
    successes = 0
    total_nfe = 0

    for _ in range(runs):
        best, nfe = genetic_algorithm(
            pop_size, generations, config, mutation_rate, stop_count
        )

        total_nfe += nfe

        if abs(best - config.optimum) < 0.01:
            successes += 1

    return (successes / runs) * 100, total_nfe / runs
