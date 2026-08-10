from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj_list = defaultdict(list)

        for s, d, w in edges:
            adj_list[s].append((d, w))

        minheap = [(0, src)]
        shortest_path = {}

        while minheap:
            distance, node = heapq.heappop(minheap)

            if node in shortest_path:
                continue

            shortest_path[node] = distance

            for neighbor, weight in adj_list[node]:
                if neighbor not in shortest_path:
                    heapq.heappush(
                        minheap,
                        (distance + weight, neighbor)
                    )

        return shortest_path