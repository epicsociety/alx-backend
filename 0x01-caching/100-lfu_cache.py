#!/usr/bin/env python3
"""
A caching system
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class inherist from BaseCaching
    Adds and retrieves an item from Cache
    """
    def __init__(self):
        """ Initializes the child class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_frequency = {}

    def put(self, key, item):
        """ Add an item to the self.cache_data
        Parameters:
        Key:
        Item:
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_keys = [k for k, v in self.access_frequency.items() if v == min(self.access_frequency.values())]
                lru_key = min(self.cache_data, key=lambda k: self.cache_data[k])
                key_to_discard = min(lfu_keys, key=lambda k: self.cache_data[k])
                print("DISCARD: {}".format(key_to_discard))
                self.cache_data.pop(key_to_discard)
                del self.access_frequency[key_to_discard]

            self.cache_data[key] = item
            self.access_frequency[key] = 1

    def get(self, key):
        """ Return the value from the self.cache_data dict
        given the key of the item
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            self.access_frequency[key] += 1
            return value
        return None
