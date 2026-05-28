class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            global_sum = max(global_sum, local_sum + nums[i])
        return global_sum