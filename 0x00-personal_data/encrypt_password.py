#!/usr/bin/env python3
""" Encrypts password using bycrypt"""

import bcrypt


def hash_password(password: str) -> str:
    """Uses hashpw to hash a password"""
    password_bytes: bytes = password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hash: bytes = bcrypt.hashpw(password_bytes, salt)

    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password is similar to hashed_password"""
    hash: bytes = hash_password(password)
    if hashed_password == hash:
        return True
    return False
