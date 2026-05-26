class Solution:
    def reverseBits(self, n: int) -> int:
        for _ in range(32):
            d = n & 1
            n >>= 1
            ans = ans | d
            ans <<= 1
        return ans