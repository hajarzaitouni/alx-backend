#!/usr/bin/env python3
""" Define MRUCache class """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    create MRUCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ add item in the cache using MRU Cache policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_key = self.stack.pop()
                del self.cache_data[most_key]
                print(f"DISCARD: {most_key}")
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ get the value by key """
        if key is None or key not in self.cache_data:
            return None
        self.stack.remove(key)
        self.stack.append(key)
        return self.cache_data[key]
