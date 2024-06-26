#!/usr/bin/env python3
""" Define FIFOCache class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    create FIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ Initialaize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add item to the cache """
        if key is not None and item is not None:
            if (key not in self.cache_data and
                    len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ get the value by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
