class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] +=1
            if hashmap[x] > 1:
                return True

        return False