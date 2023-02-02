#!/usr/bin/python3
"""Returns the sum of a list consisting of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list consisting of integers and floats"""
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
