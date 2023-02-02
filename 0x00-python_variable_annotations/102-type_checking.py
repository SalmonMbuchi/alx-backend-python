#!/usr/bin/env python3
"""Type checking"""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Validate types"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
