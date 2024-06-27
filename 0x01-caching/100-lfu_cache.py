#!/usr/bin/env python3
""" Define LFUCache class """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    create LFUCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.queue = []
        self.frequency = {}

    def put(self, key, item):
        """ add item in the cache using MRU Cache policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_fr = min(self.frequency.values())
                    lfu_key = [
                        k for k, val in self.frequency.items()
                        if val == least_fr
                        ]
                    if len(lfu_key) > 1:
                        lru_key = None
                        for k in self.queue:
                            if k in lfu_key:
                                lru_key = k
                                break
                    else:
                        lru_key = lfu_key[0]

                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    self.queue.remove(lru_key)
                    print(f"DISCARD: {lru_key}")

                self.frequency[key] = 1

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get the value by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
