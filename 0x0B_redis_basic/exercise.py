#!/usr/bin/env python3
"""Cache class provides methods to store and retrieve data in a Redis
database. It uses random key by UUID to store data.
"""
import redis
import uuid
from typing import Union


class Cache():
    """Cache class for interacting with Redis.
    """
    def __init__(self):
        """Stores an instance of Redis client and flushes the instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a rajdom key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
