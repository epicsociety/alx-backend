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
        """ Add an item to the self.cache_data
        Parameters:
        Key:
        Item:
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(lru_key))
                self.cache_data.pop(lru_key)

            self.cache_data[key] = item

    def get(self, key):
        """ Return the value from the self.cache_data dict
        given the key of the item
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
