from dataclasses import dataclass
from typing import Callable

from fitness_functions import aluffi_pentini, three_camel_back


@dataclass
class FunctionConfig:
    func: Callable
    bounds: tuple
    optimum: float
    n: int


FUNCTIONS_CONFIG = {
    "AP": FunctionConfig(func=aluffi_pentini, bounds=(-10, 10), optimum=-0.3523, n=2),
    "CB3": FunctionConfig(func=three_camel_back, bounds=(-5, 5), optimum=0.0, n=2),
}
