from create_population import create_population
from fitness_functions import aluffi_pentini, three_camel_back
from config_type import FunctionConfig
from selection import crossover, mutate, selection

# =========================
# CONFIGURAÇÕES
# =========================
POP_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.1
FUNCTIONS_CONFIG = {
    "AP": FunctionConfig(func=aluffi_pentini, bounds=(-10, 10), optimum=-0.3523, n=2),
    "CB3": FunctionConfig(func=three_camel_back, bounds=(-5, 5), optimum=0.0, n=2),
}
NFE = 0


def genetic_algorithm(
    pop_size, generations, function_config: FunctionConfig, mutation_rate
):
    population = create_population(pop_size, function_config.bounds, function_config.n)
    fitness = function_config.func
    best = None

    for gen in range(generations):
        new_population = []

        for _ in range(pop_size):
            p1 = selection(population, fitness)
            p2 = selection(population, fitness)

            child = crossover(p1, p2)
            child = mutate(child, mutation_rate, function_config.bounds)

            new_population.append(child)

        population = new_population
        best = min(population, key=lambda ind: evaluate(ind, fitness))

    return best, fitness(best)


def success_rate(function_config: FunctionConfig, runs=100):
    successes = 0

    for _ in range(runs):
        best, value = genetic_algorithm(
            POP_SIZE, GENERATIONS, function_config, MUTATION_RATE
        )

        if abs(value - function_config.optimum) < 0.01:
            successes += 1

    return (successes / runs) * 100


def evaluate(ind, fitness):
    global NFE
    NFE += 1
    return fitness(ind)


# =========================
# EXECUÇÃO
# =========================
sr = success_rate(FUNCTIONS_CONFIG["AP"])
print(f"Taxa de sucesso AP: {sr}%")
print("NFE:", NFE)
