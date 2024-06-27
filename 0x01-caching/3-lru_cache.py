#!/usr/bin/env python3
""" Define LRUCache class """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    create LRUCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ add item in the cache using LRU Cache policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_key = self.queue.pop(0)
                del self.cache_data[least_key]
                print(f"DISCARD: {least_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ get the value by key """
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
