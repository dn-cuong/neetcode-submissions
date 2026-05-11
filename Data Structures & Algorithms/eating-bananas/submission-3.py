class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            curr = 0
            for x in piles:
                curr += math.ceil(x / mid)
            if curr <= h:
                high = mid
            else:
                low = mid + 1
        return low