#!/usr/bin/env python3
"""Cache class provides methods to store and retrieve data in a Redis
database. It uses random key by UUID to store data.
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes,
                                                    int, float, None]:
        """Retrieves data from Redis.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieves data from Redis as a string.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if data:
            return data.decode('utf-8')
        return None

    def get_int(self, key: str) -> int:
        """Retrieves data and converts into integer.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return self.get(key, fn=int)
