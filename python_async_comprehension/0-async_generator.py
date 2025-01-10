#!/usr/bin/env python3
"""
Coroutine that takes no argumens and yields 10 random numbers.
"""
import asyncio
import random


async def async_generator() -> float:
    """
    Yields 10 random floats between the numbers 0-10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
