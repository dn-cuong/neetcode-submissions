class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        move = [[1,0], [-1,0], [0,1], [0, -1]]
        
        queue = deque()
        visit = set()

        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    visit.add((i,j))

        level = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit or grid[nr][nc] != 1:
                        continue
                    
                    fresh -= 1
                    queue.append((nr, nc))
                    visit.add((nr, nc))

            level += 1

        return level if fresh == 0 else -1
