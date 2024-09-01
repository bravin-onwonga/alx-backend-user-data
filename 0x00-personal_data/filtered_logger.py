#!/usr/bin/env python3
"""Filter using re.sub"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filters data and returns a message"""
    for key in fields:
        message = re.sub(rf"{key}=[^{separator}]*",
                         f'{key}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Instantiates """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """"filter values in incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Create and configure a logger """
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Connect to db using mysql.connector """
    passwd = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    name = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(
        host=host,
        database=db_name,
        user=name,
        password=passwd)
    return conn


def main() -> None:
    """ Read and filter data """
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')

    for user in cursor:
        msg = f"name={user[0]}; email={user[1]}; phone={user[2]}; " +\
            f"ssn={user[3]}; password={user[4]};ip={user[5]}; " +\
            f"last_login={user[6]}; user_agent={user[7]};"
        print(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
