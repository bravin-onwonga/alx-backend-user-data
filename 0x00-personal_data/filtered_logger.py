#!/usr/bin/env python3
"""Filter using re.sub"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filters data and returns a message"""
    for key in fields:
        message = re.sub(rf"{key}=[^{separator}]*",
                         f'{key}={redaction}', message)
    return message
