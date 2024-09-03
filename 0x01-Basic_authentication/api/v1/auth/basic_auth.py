#!/usr/bin/env python3
""" Class inheriting from auth """

import base64
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

    def decode_base64_authorization_header(self,
                                           base64_auth_header: str) -> str:
        """ Decode value of a Base64 string
        Returns
            decoded value of the string
        """
        if not base64_auth_header:
            return None
        if type(base64_auth_header) != str:
            return None

        try:
            decoded_bytes = base64.b64decode(base64_auth_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_auth_header: str) -> (str, str):
        """ Extract credentials """
        if not decoded_base64_auth_header:
            return (None, None)
        if isinstance(decoded_base64_auth_header, str) == False:
            return (None, None)
        if ':' not in decoded_base64_auth_header:
            return (None, None)
        user_data = decoded_base64_auth_header.split(':')
        return (user_data[0], user_data[1])
