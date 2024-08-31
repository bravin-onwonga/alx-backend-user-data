#!/usr/bin/env python3
"""Filter using re.sub"""
import re


def filter_datum(fields, redaction, message, separator):
    """filters data and returns a message"""
    for key in fields:
        message = re.sub(rf"{key}=[^{separator}]*",
                         f'{key}={redaction}{separator}', message)
    return message
