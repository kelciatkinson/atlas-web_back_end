#!/usr/bin/env python3
"""
Type-annotated function that takes a list of floats
and integers as an argument and returns their sum as a float.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum in a float of a list of given integers and floats."""
    return sum(mxd_lst)
