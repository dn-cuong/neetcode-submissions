class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        ans = 0

        def dfs(node):
            visit.add(node)

            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1

        return ans