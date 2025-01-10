#!/usr/bin/env python3
"""
Dynmically import previous python file and coroutine
that executes async_comprehension four times in parallel
using asyncio.gather.
"""
import asyncio
import importlib.util
import time


module_name = "async_comprehension"
file_path = "1-async_comprehension.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime and returns it.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
