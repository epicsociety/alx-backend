#!/usr/bin/env python3
"""
A caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Class inherist from BaseCaching
    Adds and retrieves an item from Cache
    """
    def __init__(self):
        """ Initializes the child class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the self.cache_data
        Parameters:
        Key:
        Item:
        """

        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped = self.cache_data.popitem()
                print("DISCARD: {}".format(popped[0]))
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value from the self.cache_data dict
        given the key of the item
        """
        if key is None:
            return None
        return self.cache_data.get(key)
