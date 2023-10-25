#!/usr/bin/env python3
"""
A caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class inherist from BaseCaching
    Adds and retrieves an item from Cache
    """
    def __init__(self):
        """ Initializes the child class
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the self.cache_data
        Parameters:
        Key:
        Item:
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value from the self.cache_data dict
        given the key of the item
        """
        if key is None:
            return None
        return self.cache_data.get(key)
