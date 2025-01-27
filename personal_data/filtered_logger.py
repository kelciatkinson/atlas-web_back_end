#!/usr/bin/env python3
"""
Module for filtering sensitive info from log messages.
"""
import re
import typing


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f"\\1={redaction}", message)
