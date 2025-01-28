#!/usr/bin/env python3
"""
Module for filtering sensitive info from log messages.
"""
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, f"\\1={redaction}", message)


def get_logger() -> logging.Logger:
    """Creates a logger for processing user data.
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Method returns filtered log record of sensitive fields.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)
