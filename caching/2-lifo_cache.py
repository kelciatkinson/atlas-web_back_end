#!/usr/bin/env python3
"""
Caching system inheriting from base_caching.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a caching system that
    stores and retrieves items from caache.
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Method to store items in cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.queue.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        Method to retrieve items from cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
