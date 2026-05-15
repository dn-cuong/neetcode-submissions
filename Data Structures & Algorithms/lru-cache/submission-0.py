from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = deque()
    def get(self, key: int) -> int:
        for x in self.cache:
            i, j = x
            if i == key:
                return j
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache.append([key, value])
        if len(self.cache) > self.capacity:
            self.cache.popleft()
        

