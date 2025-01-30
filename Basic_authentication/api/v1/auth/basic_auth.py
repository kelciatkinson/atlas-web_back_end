#!/usr/bin/env python3
"""Module for authentication
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Empty class inherting from Auth.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 part of Authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) -> (
                                 str, str):
        """Returns user email and password from Bas64 decoded value.
        """

        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        (user_email,
         user_password) = decoded_base64_authorization_header.split(':', 1)
        return (user_email, user_password)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            if not users:
                return None

            user = users[0]

            if user.is_valid_password(user_pwd):
                return user

        except Exception:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the User instance for a request.
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(auth_header)
        if base64_header is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_header)
        if decoded_auth is None:
            return None

        (user_email, user_pwd) = self.extract_user_credentials(decoded_auth)

        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
