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
        if not path:
            return True

        last_idx = len(path) - 1

        if path[last_idx] != '/':
            path = path + '/'

        if excluded_paths == [] or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None """
        return None
