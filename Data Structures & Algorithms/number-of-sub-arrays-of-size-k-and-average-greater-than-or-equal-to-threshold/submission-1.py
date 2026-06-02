class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curSum = 0
        res = 0

        for R in range(len(arr)):
            curSum += arr[R]

            if R - L + 1 > k:
                curSum -= arr[L]
                L += 1

            if R - L + 1 == k:
                if curSum >= k * threshold:
                    res += 1

        return res