#!/usr/bin/env python3
"""Modle for authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class to manage API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False - path and exlduded_paths will be used later.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None - request will be the Flask request object.
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object
        """
        return None

