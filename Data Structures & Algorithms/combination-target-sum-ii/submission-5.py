class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [] , []
        candidates.sort()
        def backtracking(start, s):
            if s == target and sol not in res:
                res.append(sol[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sol.append(candidates[i])
                backtracking(i+1, s + candidates[i])
                sol.pop()

        backtracking(0, 0)

        return res