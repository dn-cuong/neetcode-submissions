from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Max heap: (-frequency, task)
        max_heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(max_heap)

        # Cooldown queue:
        # (available_time, remaining_frequency, task)
        cooldown = deque()

        time = 0

        while max_heap or cooldown:

            # Move tasks whose cooldown has finished
            while cooldown and cooldown[0][0] <= time:
                available_time, freq, task = cooldown.popleft()
                heapq.heappush(max_heap, (-freq, task))

            # Execute a task if one is available
            if max_heap:
                neg_freq, task = heapq.heappop(max_heap)
                freq = -neg_freq

                freq -= 1

                # If this task still has remaining instances,
                # put it into cooldown
                if freq > 0:
                    cooldown.append((time + n + 1, freq, task))

            time += 1

        return time