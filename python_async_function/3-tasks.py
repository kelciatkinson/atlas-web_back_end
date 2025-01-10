#!/usr/bin/env python3
"""
Dynamically import previous python file and function
that creates a task.
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


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer and returns an asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
