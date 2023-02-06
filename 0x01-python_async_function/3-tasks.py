#!/usr/bin/env python3
"""Return a asyncio.Task"""

import asyncio
from typing import Type
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Type[asyncio.Task]:
    # num = asyncio.create_task(wait_random(max_delay))
    loop = asyncio.get_running_loop()
    return loop.create_task(wait_random(max_delay))
