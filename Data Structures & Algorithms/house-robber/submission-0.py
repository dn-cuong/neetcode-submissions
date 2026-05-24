class Solution:
    def rob(self, nums: List[int]) -> int:
        m1 = sum(nums[i] for i in range(0,len(nums), 2))
        m2 = sum(nums[i] for i in range(1,len(nums), 2))

        return max(m1, m2)