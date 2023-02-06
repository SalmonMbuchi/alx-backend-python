#!/usr/bin/env python3
"""Execute multiple coroutines"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of delays"""
    myList = []
    newList = []
    for i in range(n):
        num = asyncio.create_task(wait_random(max_delay))
        myList.append(num)
    for res in asyncio.as_completed(myList):
        compl = await res
        newList.append(compl)
    return newList
