import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for right in range(len(nums)):
            # value, index
            heapq.heappush(heap, (-nums[right], right))

            # Remove elements outside the current window
            while heap[0][1] <= right - k:
                heapq.heappop(heap)

            # Window has reached size k
            if right >= k - 1:
                ans.append(-heap[0][0])

        return ans