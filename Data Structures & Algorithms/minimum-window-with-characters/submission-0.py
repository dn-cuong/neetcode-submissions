from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window = {}
        hash_t = Counter(t)

        having = 0
        need = len(hash_t)

        left = 0
        res = ""
        resLen = float("inf")

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            # Character just became fully satisfied
            if s[right] in hash_t and window[s[right]] == hash_t[s[right]]:
                having += 1

            # Try to shrink the window
            while having == need:
                if right - left + 1 < resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1

                # Remove left character
                if s[left] in hash_t and window[s[left]] == hash_t[s[left]]:
                    having -= 1

                window[s[left]] -= 1
                left += 1

        return res