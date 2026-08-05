class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            while len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    hashmap.pop(s[left])
                left += 1

            ans = max(ans, right - left + 1)

        return ans