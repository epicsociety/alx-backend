#!/usr/bin/env python3
"""
A caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Initialize the class
    """
    def __init__(self):
        """ Initialize the child class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
