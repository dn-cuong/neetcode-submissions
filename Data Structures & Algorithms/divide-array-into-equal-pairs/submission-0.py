class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for cnt in count.values():
            if cnt % 2 == 1:
                return False

        return True