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

        level = -1
        while queue and fresh >0 :
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    grid[r][c] == 2
                    fresh -=1
                for dr, dc in move:
                    if min(r+dr, c+dc) < 0 or r + dr >= ROWS or c + dc >= COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] in set([0,2]):
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))

            level +=1

        return level if fresh == 0 else -1

            

            