class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(i, temp):
            if len(temp) == k:
                ans.append(temp[:])
                return

            for j in range(i+1, n+1):
                temp.append(j)
                backtracking(j, temp)
                temp.pop()


        for i in range(1, n+1):
            backtracking(i, [i])

        return ans