class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def backtrack(i, curr, path):

            if curr == target:
                res.append(path[:])
                return

            if i >= len(nums) or curr > target:
                return

            path.append(nums[i])
            backtrack(i, curr + nums[i], path)

            path.pop()

            backtrack(i + 1, curr, path)

        backtrack(0, 0, [])

        return res