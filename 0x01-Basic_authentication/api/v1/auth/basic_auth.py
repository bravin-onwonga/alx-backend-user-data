#!/usr/bin/env python3
""" Class inheriting from auth """

import base64
from api.v1.auth.auth import Auth
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_b64_auth_header: str) -> (str, str):
        """ Extract credentials """
        if not decoded_b64_auth_header:
            return (None, None)
        if isinstance(decoded_b64_auth_header, str) is False:
            return (None, None)
        if ':' not in decoded_b64_auth_header:
            return (None, None)
        user_data = decoded_b64_auth_header.split(':')
        email = user_data[0]
        pwd = ""
        for data in user_data[1:]:
            if pwd != "":
                pwd += ':'
            pwd += data

        return (email, pwd)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Finds user based on credentials
        Return
            User instance
        """
        from models.user import User

        if not user_email or not user_pwd:
            return None

        user = User().search({'email': user_email})

        if len(user) > 0:
            user = user[0]
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets current user """
        if request:
            basic_str = self.authorization_header(request)

            if not basic_str:
                return None

            encoded_pwd = self.extract_base64_authorization_header(basic_str)

            if not encoded_pwd:
                return None
            decoded_pwd = self.decode_base64_authorization_header(encoded_pwd)

            if not decoded_pwd:
                return None

            user_info = self.extract_user_credentials(decoded_pwd)
            user = self.user_object_from_credentials(user_info[0],
                                                     user_info[1])
            if user:
                return ([user.to_json()])
            return None
