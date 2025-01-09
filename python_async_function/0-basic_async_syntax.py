#!/usr/bin/env python3
import asyncio
import random
"""
Defines an aynchronous coroutine.
"""


async def wait_random(max_delay: int = 10):
    """
    Asynchronous coroutine that takes in an integer argument
    and waits for a random delay between 0 and max_delay and
    eventually returns it.
    """
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
