class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if count ^ x:
                return count
            count +=1