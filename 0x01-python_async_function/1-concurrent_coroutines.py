#!/usr/bin/env python3
"""Execute multiple coroutines"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """returns a list of delays"""
    myList = []
    for i in range(n):
        num = await wait_random(max_delay)
        myList.append(num)
    return myList
