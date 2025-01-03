#!/usr/bin/env pythion3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
