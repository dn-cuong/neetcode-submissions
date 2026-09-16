class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        def dfs(i, curr):
            nonlocal ans
            if i == len(nums):
                return
            if i == len(nums) - 1 and curr == target:
                ans += 1

            dfs(i+1, curr + nums[i])
            dfs(i+1, curr + nums[i] * -1)


        dfs(0, nums[0])            
        dfs(0, -1*nums[0])    

        return ans        
