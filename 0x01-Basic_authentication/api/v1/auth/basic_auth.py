#!/usr/bin/env python3
""" Class inheriting from auth """

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class inheriting from Auth
    """
    def __init__(self) -> None:
        """ Instantiates an instance """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Basic - Base64 part """
        if not authorization_header:
            return None
        if type(authorization_header) != str:
            return None
        authorization_header_lst = authorization_header.split(" ")

        if (len(authorization_header_lst) != 2):
            return None

        key = authorization_header_lst[0]
        value = authorization_header_lst[1]

        if key != 'Basic':
            return None
        return value
