#!/usr/bin/env python3
"""Cache class provides methods to store and retrieve data in a Redis
database. It uses random key by UUID to store data.
"""
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """Counts number of times method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments count and calls original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """Cache class for interacting with Redis.
    """
    def __init__(self):
        """Stores an instance of Redis client and flushes the instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a rajdom key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes,
                                                    int, None]:
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
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves data and converts into integer.
        """
        data = self._redis.get(key)
        return self.get(key, fn=int)
