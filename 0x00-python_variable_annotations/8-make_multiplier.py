#!/usr/bin/env python3
"""Returns a function that multiplies a float by multiplier"""
from typing import Callable

f = make_multiplier(multiplier)


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return f(multiplier * multiplier)
