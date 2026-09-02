class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        ans = 0
        def dfs(node, par):

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs(nei, node)
            return True

        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                ans += 1

        return ans