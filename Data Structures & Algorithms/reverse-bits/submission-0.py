class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        count = 0
        while n:
            d = n & 1
            n >>= 1
            ans = ans | d
            ans <<= 1
            count += 1
        return ans << (32- count - 1)