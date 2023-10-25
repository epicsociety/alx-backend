#!/usr/bin/env python3
"""
A caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class inherist from BaseCaching
    Adds and retrieves an item from Cache
    """
    def __init__(self):
        """ Initializes the child class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_order = set()

    def put(self, key, item):
        if key is not None and item is not None:
            # If cache is at max capacity, remove least recently used
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = next(iter(self.access_order))
                self.cache_data.pop(lru_key)
                self.access_order.remove(lru_key)

            # Add item to cache and update access order
            self.cache_data[key] = item
            self.access_order.add(key)

    def get(self, key):
        if key in self.cache_data:
            # Move accessed item to the end of the access order
            self.access_order.remove(key)
            self.access_order.add(key)
            return self.cache_data[key]
        return None
