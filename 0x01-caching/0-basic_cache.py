#!/usr/bin/env python3
"""
Define BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    create BasicCache that inherits from BaseCaching
    and is a caching system.
    """
    def put(self, key, item):
        """ add item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get the value by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
