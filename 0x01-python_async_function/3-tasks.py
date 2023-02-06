#!/usr/bin/env python3
"""Return a asyncio.Task"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> object:
    # num = asyncio.create_task(wait_random(max_delay))
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
