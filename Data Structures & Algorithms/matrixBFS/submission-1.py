class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))
        length = 0
        move = [[0,1], [0,-1], [1, 0], [-1, 0]] # move right, left, down, up
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS -1 and c == COLS -1:
                    return length
                for x,y in move:
                    if min(r+x, c+y) < 0 or r + x >= ROWS or c + y >= COLS or (r+x, c+y) in visit or grid[r+x][c+y] == 1:
                        continue
                    queue.append((r+x, c+y))
                    visit.add((r+x, c+y))
            length +=1
        return -1
