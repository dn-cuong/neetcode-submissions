class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        ans = 0
        while k > 0:
            ans = heapq.heappop(nums)
            k -=1

        return -ans        