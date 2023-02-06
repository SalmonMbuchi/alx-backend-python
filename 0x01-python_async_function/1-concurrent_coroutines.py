#!/usr/bin/env python3
"""Execute multiple coroutines"""

# import wait_random from './0-basic_async_syntax.py'
# import random
# import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """returns a list of delays"""
    myList = []
    for i in range(n):
        num = await wait_random(max_delay)
        myList.append(num)
    return myList
