#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime of function ran 4 times in parallel"""
    start = time.perf_counter()
    res = await asyncio.gather(async_comprehension(), async_comprehension(),
                               async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start
    return elapsed
