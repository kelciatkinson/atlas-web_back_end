#!/usr/bin/env python3
"""
Caching system inheriting from base_caching.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Implements a caching system that
    stores and retrieves items from caache.
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        self.cache_data[key] = item
        self.queue.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.queue.pop(0)
            print(f"DISCARD: {discard}")
            del self.cache_data[discard]

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
