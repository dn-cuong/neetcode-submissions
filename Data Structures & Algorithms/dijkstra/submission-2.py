from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj_list = defaultdict(list)

        for s, d, w in edges:
            adj_list[s].append((d, w))

        minheap = [(0, src)]

        shortest_path = {i: -1 for i in range(n)}

        while minheap:
            distance, node = heapq.heappop(minheap)

            # Already found shortest distance
            if shortest_path[node] != -1:
                continue

            shortest_path[node] = distance

            for neighbor, weight in adj_list[node]:
                if shortest_path[neighbor] == -1:
                    heapq.heappush(
                        minheap,
                        (distance + weight, neighbor)
                    )

        return shortest_path