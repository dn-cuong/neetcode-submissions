class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                length = min(length, r-l+1)
                curr -= nums[l]
                l+=1
        return 0 if length == float('inf') else length