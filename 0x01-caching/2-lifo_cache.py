#!/usr/bin/env python3
""" Define LIFOCache class """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    create LIFOCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ add key in the cache """
        if key is not None and item is not None:
            if (key not in self.cache_data and
                    len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ get the value by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
