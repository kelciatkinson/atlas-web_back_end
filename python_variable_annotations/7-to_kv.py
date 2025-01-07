#!/usr/bin/env python3
"""
Type-annotated function that takes a string and an int OR float as arguments
and returns a tuple.
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns tuple of string, and square of the number v"""
    return (k, v ** 2)
