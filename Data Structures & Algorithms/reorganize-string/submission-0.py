from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        hashmap = Counter(s)
        priority_queue = []

        for x in hashmap:
            heapq.heappush(priority_queue, (-hashmap[x], x))

        ans = ""

        while len(priority_queue) >= 2:
            freq1, char1 = heapq.heappop(priority_queue)
            freq2, char2 = heapq.heappop(priority_queue)

            ans += char1
            ans += char2

            freq1 += 1
            freq2 += 1

            # còn character thì push lại
            if freq1 < 0:
                heapq.heappush(priority_queue, (freq1, char1))

            if freq2 < 0:
                heapq.heappush(priority_queue, (freq2, char2))

        # còn 1 character
        if priority_queue:
            freq, char = heapq.heappop(priority_queue)

            if -freq > 1:
                return ""

            ans += char

        return ans