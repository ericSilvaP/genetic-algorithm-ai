from config_type import FUNCTIONS_CONFIG
from genetic_alg import success_rate

POP_SIZE = 50
GENERATIONS = 200
STOP_COUNT = 15

sr, avg_nfe = success_rate(
    FUNCTIONS_CONFIG["AP"], POP_SIZE, GENERATIONS, STOP_COUNT, mutation_rate=0.25
)

print("--- Aluffi-Pentini ---")
print(f"Taxa de acerto: {sr}%")
print(f"NFE médio: {avg_nfe}")
