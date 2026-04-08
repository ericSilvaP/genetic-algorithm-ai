from config_type import FUNCTIONS_CONFIG
from genetic_alg import success_rate


POP_SIZE = 50
GENERATIONS = 200
STOP_COUNT = 5

sr, avg_nfe = success_rate(FUNCTIONS_CONFIG["CB3"], POP_SIZE, GENERATIONS, STOP_COUNT)

print("--- Camel Back Hump 3 ---")
print(f"Taxa de acerto: {sr}%")
print(f"NFE médio: {avg_nfe}")
