#!/usr/bin/env python3
"""
Dynmically import previous python file and coroutine
that takes no arguments that will collect 10 random numbers
using an async comprehensing over async_generator.
"""
import asyncio
import importlib.util
import typing


module_name = "async_generator"
file_path = "0-async_generator.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

async_generator = module.async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Collect 10 random numbers using an async comprehensing over async_generator
    then return 10 random numbers.
    """
    return [num async for num in async_generator()]
