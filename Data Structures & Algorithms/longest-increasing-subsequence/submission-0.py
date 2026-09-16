class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > curr and nums[j] == min(nums[j:]):
                    curr = nums[j]
                    dp[i] += 1
        return max(dp)