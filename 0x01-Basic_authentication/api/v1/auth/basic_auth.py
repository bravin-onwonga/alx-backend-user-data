#!/usr/bin/env python3
""" Class inheriting from auth """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class inheriting from Auth
    """
    def __init__(self):
        """ Instantiates an instance """
        super().__init__()
