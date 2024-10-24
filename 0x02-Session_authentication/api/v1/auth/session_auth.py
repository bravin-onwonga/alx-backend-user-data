#!/usr/bin/env python3
""" Session authentication class """
from api.v1.auth.auth import Auth
from uuid import uuid4 as uid


class SessionAuth(Auth):
    """ Sessions class """
    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        """ Create a new session """
        if not user_id or not isinstance(user_id, str):
            return None
        key = uid()
        self.user_id_by_session_id[key] = user_id
        return key        
