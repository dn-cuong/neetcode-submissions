from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        minheap = [(0, src)]

        adj_list = defaultdict(list)

        for s, d, w in edges:
            adj_list[s].append((d, w))

        shortest_path = {}
        while minheap:
            w, n = heapq.heappop(minheap)

            if n in shortest_path:
                continue

            shortest_path[n] = w

            for i,j in adj_list[n]:
                if i not in shortest_path:
                    heapq.heappush(minheap, (w+j, i))
        return shortest_path