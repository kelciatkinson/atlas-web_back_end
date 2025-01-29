#!/usr/bin/env python3
"""
Module contains functions to encrypt password
and check if it's hashed.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with salt.
    """
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a password matches a hashed password.
    """
    password = password.encode()
    return bcrypt.checkpw(password, hashed_password)
