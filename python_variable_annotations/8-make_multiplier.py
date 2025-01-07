#!/usr/bin/env python3
"""
Type-annotated function that takes a float as an argument
and returns a function that multiplies a float by a multiplier.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns function that multiplies float variable by itself."""
    def multiply(n: float) -> float:
        """Multiplies float variable by itself."""
        return n * multiplier 
    return multiply