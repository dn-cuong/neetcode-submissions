class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix sum
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(len(prefix)-1):
            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        return -1