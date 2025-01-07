#!/usr/bin/env python3
import typing
"""
Type-annotated function that takes a list of floats
as an argument and returns their sum as a float.
"""


def sum_list(input_list: typing.List[float]) -> float:
    """Returns the sum of a list of given floats."""
    return sum(input_list)
