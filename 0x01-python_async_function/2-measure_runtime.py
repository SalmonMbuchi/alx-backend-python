#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the execution time for wait_n(n, max_delay)"""
    start = time.time()
    myList = asyncio.create_task(wait_n(n, max_delay))
    elapsed = (time.time() - start) / n
    return elapsed
