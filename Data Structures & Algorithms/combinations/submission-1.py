class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(i, temp):
            if len(temp) == k:
                ans.append(temp[:])
                return

            for j in range(i, n+1):
                temp.append(j)
                backtracking(j+1, temp)
                temp.pop()


        backtracking(1, [])

        return ans