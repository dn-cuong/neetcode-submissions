class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2

        def dfs(i, curr):
            if curr == target:
                return True

            if i == len(nums):
                return False

            return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

        return dfs(0, 0)