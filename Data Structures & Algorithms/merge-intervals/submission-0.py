from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        dq = deque()

        for interval in intervals:
            if not dq or interval[0] > dq[-1][1]:
                dq.append(interval)
            else:
                dq[-1][1] = max(dq[-1][1], interval[1])

        return list(dq)