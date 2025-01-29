#!/usr/bin/env python3
"""Module for authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class to manage API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False - path and exlduded_paths will be used later.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                if path == excluded_path:
                    return False
            else:
                if path == excluded_path + "/":
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None - request will be the Flask request object.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object
        """
        return None
