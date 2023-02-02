#!/usr/bin/env python3
"""Return sum of values in a list as a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of values in a list as a float"""
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
