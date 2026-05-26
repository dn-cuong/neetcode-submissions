class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            d = n & 1
            n >>= 1
            ans = (ans << 1) | d
        return ans