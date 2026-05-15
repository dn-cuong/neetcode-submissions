from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = deque()

    def _find_and_remove(self, key):
        for i in range(len(self.cache)):
            k, v = self.cache[i]
            if k == key:
                self.cache.remove(self.cache[i])
                return v
        return -1

    def get(self, key: int) -> int:
        value = self._find_and_remove(key)
        if value == -1:
            return -1

        self.cache.append([key, value])
        return value

    def put(self, key: int, value: int) -> None:
        self._find_and_remove(key)

        self.cache.append([key, value])

        if len(self.cache) > self.capacity:
            self.cache.popleft()