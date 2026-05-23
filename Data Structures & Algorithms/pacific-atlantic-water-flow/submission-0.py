from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r, c, ocean):
            queue = deque()
            queue.append((r, c))

            visit = set()
            visit.add((r, c))

            while queue:
                row, col = queue.popleft()

                # Pacific
                if ocean == "pac":
                    if row == 0 or col == 0:
                        return True

                # Atlantic
                if ocean == "atl":
                    if row == ROWS - 1 or col == COLS - 1:
                        return True

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and
                        heights[nr][nc] <= heights[row][col]
                    ):
                        visit.add((nr, nc))
                        queue.append((nr, nc))

            return False

        res = []

        for r in range(ROWS):
            for c in range(COLS):

                if bfs(r, c, "pac") and bfs(r, c, "atl"):
                    res.append([r, c])

        return res