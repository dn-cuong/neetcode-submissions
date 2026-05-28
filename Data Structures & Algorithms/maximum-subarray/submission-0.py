class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            local_sum = max(nums[i], local_sum + nums[i-1])
            global_sum = max(global_sum, local_sum)
        return global_sum