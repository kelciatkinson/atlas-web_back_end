#!/usr/bin/env python3
"""
Caching system inheriting from base_caching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a basic caching system that
    stores and retrieves items from caache.
    """

    def put(self, key, item):
        """
        Method to store items in cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method to retrieve items from cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
