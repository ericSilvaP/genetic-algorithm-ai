from create_population import create_population
from config_type import FUNCTIONS_CONFIG, FunctionConfig
from selection import crossover, mutate, selection

NFE = 0


def genetic_algorithm(
    pop_size,
    generations,
    function_config: FunctionConfig,
    mutation_rate=None,
    best_fit_stop_count=10,
):
    population = create_population(pop_size, function_config.bounds, function_config.n)
    fitness = function_config.func
    best_fitness = 0
    best_continous_count = 0

    for gen in range(generations):
        best_gen_fitness = evaluate(
            min(population, key=lambda ind: evaluate(ind, fitness)), fitness
        )

        if gen == 0 or best_gen_fitness < best_fitness:
            best_fitness = best_gen_fitness
            best_continous_count = 0
        else:
            best_continous_count += 1

        if best_continous_count >= best_fit_stop_count:
            break

        # Gerar nova população
        new_population = []
        for _ in range(pop_size):
            p1 = selection(population, fitness)
            p2 = selection(population, fitness)

            child = crossover(p1, p2)
            if mutation_rate:
                child = mutate(child, mutation_rate, function_config.bounds)

            new_population.append(child)

        population = new_population

    return best_fitness


def success_rate(
    function_config: FunctionConfig,
    pop_size,
    generations,
    best_fit_stop_count,
    runs=100,
    mutation_rate=None,
):
    successes = 0

    for _ in range(runs):
        value = genetic_algorithm(
            pop_size, generations, function_config, mutation_rate, best_fit_stop_count
        )

        if abs(value - function_config.optimum) < 0.01:
            successes += 1

    return (successes / runs) * 100


def evaluate(ind, fitness):
    global NFE
    NFE += 1
    return fitness(ind)


# Aluffi
POP_SIZE = 50
GENERATIONS = 200
MUTATION_RATE = 0.3
BEST_FIT_STOP_COUNT = 25

runs = 100
sr = success_rate(
    FUNCTIONS_CONFIG["AP"],
    POP_SIZE,
    GENERATIONS,
    BEST_FIT_STOP_COUNT,
    runs=runs,
    mutation_rate=MUTATION_RATE,
)
print(f"Taxa de sucesso AP: {sr}%")
print("NFE:", round(NFE / runs))

# Camel Back 3
POP_SIZE = 50
GENERATIONS = 200
BEST_FIT_STOP_COUNT = 5
NFE = 0

runs = 100
sr = success_rate(
    FUNCTIONS_CONFIG["CB3"],
    POP_SIZE,
    GENERATIONS,
    BEST_FIT_STOP_COUNT,
    runs=runs,
)
print(f"Taxa de sucesso CB3: {sr}%")
print("NFE:", round(NFE / runs))
