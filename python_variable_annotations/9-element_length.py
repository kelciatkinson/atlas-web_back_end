#!/usr/bin/env python3
"""
Type-annotated function that takes a list as an argument
and returns a list of tuples that contains its contents and its length.
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    """Returns a list of tuples containing the sequence and its length."""
    return [(i, len(i)) for i in lst]
