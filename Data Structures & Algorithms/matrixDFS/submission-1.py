class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visit):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 1 or (r,c) in visit :
                return 0
            if r == len(grid) - 1 and c == len(grid[0]) -1:
                return 1

            visit.add((r,c))
            count = 0
            count += dfs(grid, r -1, c, visit) # move up
            count += dfs(grid, r +1, c, visit) # move down
            count += dfs(grid, r, c -1, visit) # left
            count += dfs(grid, r, c+1, visit) # right


            visit.remove((r,c))

            return count
        count = dfs(grid, 0,0, set())

        return count
