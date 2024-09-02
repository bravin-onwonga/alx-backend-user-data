#!/usr/bin/env python3
""" Handles authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """ authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for future use
        Returns
            False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None """
        return None
