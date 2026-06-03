class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = {}
        j = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = 1
            else:
                dct[nums[i]] +=1

            if dct[nums[i]] > 2:
                continue
            else:
                nums[j] = nums[i]
                j += 1
                k+=1
        
        return k
        

            