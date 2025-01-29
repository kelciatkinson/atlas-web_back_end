#!/usr/bin/env python3
"""
Module contains function to encrypt password.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with salt.
    """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    return hashed
