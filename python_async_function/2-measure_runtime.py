#!/usr/bin/env python3
"""
Dynamically import previous python file and function
that measures the total execution time for the wait_n function.
"""
import asyncio
import importlib.util
import typing
import time


module_name = "wait_n"
file_path = "1-concurrent_coroutines.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes a number and a delay as arguments and returns
    the total time divided by the integer given.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
