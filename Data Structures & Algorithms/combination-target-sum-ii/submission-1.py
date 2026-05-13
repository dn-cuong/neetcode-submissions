class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [] , []

        def backtracking(start, s):
            if s == target and sol not in res:
                res.append(sol[:])
                return


            for i in range(start, len(candidates)):
                sol.append(candidates[i])
                backtracking(i+1, s + candidates[i])
                sol.pop()

        backtracking(0, 0)

        return res