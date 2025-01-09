#!/usr/bin/env python3
"""
Dynmically import previous python file and asynchronous routine
that taks two arguments that will spay wait_random n times with
specified max_delay.
"""
import asyncio
import importlib.util
import typing


module_name = "wait_random"
file_path = "0-basic_async_syntax.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Return the list of all of the delays in float values
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
