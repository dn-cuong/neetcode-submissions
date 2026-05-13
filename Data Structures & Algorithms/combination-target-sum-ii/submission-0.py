class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        def backtracking(i, s):
            if s == target and sol not in res:
                res.append(sol[:])
                return

            if len(sol) == len(candidates) or s > target or i > len(candidates)-1:
                return

            sol.append(candidates[i])
            backtracking(i+1, s + candidates[i])
            sol.pop()

            backtracking(i+1, s)


            

        backtracking(0,0)

        return res
