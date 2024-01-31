#!/usr/bin/env python3
""" LIFO caching module. """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item to the cache.
        :param key: Key where the item will be stored.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.stack:
            self.stack.remove(key)
        self.stack.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        :return: The item stored in the cache or None.
        """
        return self.cache_data.get(key, None)
