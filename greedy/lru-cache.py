# https://leetcode.com/problems/lru-cache/description/
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {} # key:int -> val
        self.lru = {} # key -> last access time
        self.tm = 0

    def get(self, key: int) -> int:
        # cache hit
        if key in self.cache_dict:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache_dict[key]
        # cache miss
        return -1


    def put(self, key: int, value: int) -> None:
        # set history and lru cache: add first, and delete later. Otherwise this would delete valid cache
        self.cache_dict[key] = value
        self.lru[key] = self.tm
        self.tm += 1

        # cache operates beyond capacity, delete old cache entries to mak e room for new entries
        if len(self.cache_dict) > self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            # remove from both history and lru cache
            self.cache_dict.pop(old_key)
            self.lru.pop(old_key)
