#!/usr/bin/env python3
"""Basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """Waits for a random delay btwn 0 and max_delay and returns it"""
    num = random.uniform(0, max_delay)
    return num
