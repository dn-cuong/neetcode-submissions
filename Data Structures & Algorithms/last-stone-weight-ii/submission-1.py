class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        memo = {}

        def dfs(i, curr):
            if i == len(stones):
                return curr

            if (i, curr) in memo:
                return memo[(i, curr)]

            skip = dfs(i + 1, curr)

            take = 0
            if curr + stones[i] <= target:
                take = dfs(i + 1, curr + stones[i])

            memo[(i, curr)] = max(skip, take)

            return memo[(i, curr)]

        best = dfs(0, 0)

        return total - 2 * best