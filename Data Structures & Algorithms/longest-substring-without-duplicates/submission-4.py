class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        ans = 1
        for R in range(len(s)):
            while s[R] in window:
                ans = max(ans, R-L)
                window.remove(s[L])
                L+=1
            window.add(s[R])
        return ans if ans else 0