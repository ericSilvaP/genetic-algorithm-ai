from dataclasses import dataclass
from typing import Callable


@dataclass
class FunctionConfig:
    func: Callable
    bounds: tuple
    optimum: float
    n: int
