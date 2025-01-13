#!/usr/bin/env python3
"""
Caching system inheriting from base_caching.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a caching system that
    stores and retrieves items from caache.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Method to store items in cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Method to retrieve items from cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
