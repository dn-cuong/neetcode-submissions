class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res, sol = [], []

        def backtracking(i):

            if i > len(nums)-1:
                res.append(sol[:])
                return

            
            # Take nums[i]
            sol.append(nums[i])
            backtracking(i+1)

            # Dont take nums[i]
            sol.pop()
            

            # Check duplicate
            while i+1 < len(nums):
                if nums[i] == nums[i+1]:
                    i+=1
                else:
                    break

            backtracking(i+1)

        
        backtracking(0)

        return res