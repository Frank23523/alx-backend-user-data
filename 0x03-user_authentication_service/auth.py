#!/usr/bin/env python3
"""auth.py"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
