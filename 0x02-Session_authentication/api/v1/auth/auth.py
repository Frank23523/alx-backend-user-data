#!/usr/bin/env python3
"""auth.py"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """template for all authentication system to be implemented"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns True if the path is not in the list of strings excluded_paths
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/') + '/'
            if excluded_path.endswith('*/'):
                if path.startswith(excluded_path[:-2]):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None

        session_name = getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
