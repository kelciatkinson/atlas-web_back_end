#!/usr/bin/env python3
"""
Defines an aynchronous coroutine that takes in an integer and returns
a randomized float based on the argument given or the default value.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    and waits for a random delay between 0 and max_delay and
    eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
