#!/usr/bin/env python3
""" 
Implements a basic caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    It's a basic caching system with no limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        :param key: Key where the item will be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        :return: The item stored in the cache or None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
