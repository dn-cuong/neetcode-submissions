class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        memo = {}

        def dfs(i, curr):
            if curr == target:
                return True

            if i == len(nums) or curr > target:
                return False

            if (i, curr) in memo:
                return memo[(i, curr)]

            memo[(i, curr)] = (
                dfs(i + 1, curr + nums[i]) or
                dfs(i + 1, curr)
            )

            return memo[(i, curr)]

        return dfs(0, 0)