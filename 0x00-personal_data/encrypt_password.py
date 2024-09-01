#!/usr/bin/env python3
""" Encrypts password using bycrypt"""

import bcrypt


def hash_password(password: str) -> str:
    """Uses hashpw to hash a password"""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password_bytes, salt)

    return hash
