#!/usr/bin/env python3
"""Use low level APIs"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of delays"""
    myList = []
    newList = []
    for i in range(n):
        num = task_wait_random(max_delay)
        myList.append(num)
    for res in asyncio.as_completed(myList):
        compl = await res
        newList.append(compl)
    return newList
