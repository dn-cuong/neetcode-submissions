class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr):
            if i == len(nums):
                return 0
            if i == len(nums) - 1 and curr == target:
                return 1

            return dfs(i+1, curr + nums[i]) + dfs(i+1, curr + nums[i] * -1)

 

        return dfs(-1,0)        
