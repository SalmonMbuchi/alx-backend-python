#!/usr/bin/env python3
"""Returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def func(value: float):
        return value * multiplier

    return func
