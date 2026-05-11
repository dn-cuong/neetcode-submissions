class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, sum(piles)
        while low < high:
            mid = (low + high) // 2
            curr = 0
            for x in piles:
                curr += (x // mid)
                if x % mid != 0:
                    curr +=1
            print(mid, curr)
            if curr <= h:
                high = mid
            else:
                low = mid + 1
        return low