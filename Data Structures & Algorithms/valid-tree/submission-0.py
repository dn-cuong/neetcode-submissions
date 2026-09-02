class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:

                # Because the graph is undirected,
                # we will see our parent again.
                # That's normal, not a cycle.
                if neighbor == parent:
                    continue

                # If we see another already-visited node,
                # we found a cycle.
                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Make sure every node was reached
        return len(visited) == n