class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        maxFreq = 0
        hashmap = {}
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, hashmap[s[right]])

            while right - left - maxFreq + 1 > k:
                hashmap[s[left]] -= 1
                left += 1
            ans = max(ans, right-left +1)
        return ans
                