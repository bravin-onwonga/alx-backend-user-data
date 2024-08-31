#!/usr/bin/env python3
"""Filter using re.sub"""
import re
from typing import List, Tuple
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filters data and returns a message"""
    for key in fields:
        message = re.sub(rf"{key}=[^{separator}]*",
                         f'{key}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str]) -> None:
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """"filter values in incoming log records"""
        fields = [key for key in self.fields]
        return filter_datum(fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
