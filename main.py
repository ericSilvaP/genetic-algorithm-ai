import random
from fitness_functions import aluffi_pentini, three_camel_back
from config_type import FunctionConfig

# =========================
# CONFIGURAÇÕES
# =========================
POP_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.1
BOUNDS = (-5, 5)
FUNCTIONS_CONFIG = {
    "AP": FunctionConfig(func=aluffi_pentini, bounds=(-10, 10), optimum=-0.3523, n=2),
    "CB3": FunctionConfig(func=three_camel_back, bounds=(-5, 5), optimum=0.0, n=2),
}


# =========================
# POPULAÇÃO INICIAL
# =========================
def create_individual(bounds):
    return [random.uniform(*bounds), random.uniform(*bounds)]


def create_population(pop_size, bounds):
    return [create_individual(bounds) for _ in range(pop_size)]


# =========================
# SELEÇÃO (TORNEIO)
# =========================
def selection(pop, fitness):
    k = 3
    selected = random.sample(pop, k)
    return min(selected, key=fitness)


# =========================
# CROSSOVER (MÉDIA)
# =========================
def crossover(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


# =========================
# MUTAÇÃO
# =========================
def mutate(ind, mutation_rate, bounds):
    if random.random() < mutation_rate:
        ind[0] += random.uniform(-0.1, 0.1)
        ind[1] += random.uniform(-0.1, 0.1)

    # manter dentro dos limites
    ind[0] = max(min(ind[0], bounds[1]), bounds[0])
    ind[1] = max(min(ind[1], bounds[1]), bounds[0])

    return ind


# =========================
# ALGORITMO GENÉTICO
# =========================
def genetic_algorithm(
    pop_size, generations, function_config: FunctionConfig, mutation_rate
):
    population = create_population(pop_size, function_config.bounds)
    fitness = function_config.func

    for gen in range(generations):
        new_population = []

        for _ in range(pop_size):
            p1 = selection(population, fitness)
            p2 = selection(population, fitness)

            child = crossover(p1, p2)
            child = mutate(child, mutation_rate, function_config.bounds)

            new_population.append(child)

        population = new_population

    best = min(population, key=fitness)
    return best, fitness(best)


# =========================
# EXECUÇÃO
# =========================
best, value = genetic_algorithm(
    POP_SIZE, GENERATIONS, FUNCTIONS_CONFIG["AP"], MUTATION_RATE
)
print("Melhor solução:", best)
print("Valor:", value)
