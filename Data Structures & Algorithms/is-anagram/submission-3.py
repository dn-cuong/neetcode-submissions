from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First solution: Using hashmap to keep track of frequency of each element in two strings
        # Time complexity: O(Max(s, t))
        # Space complexity: O(max(s, t))


        s_dct = Counter(s)
        t_dct = Counter(t)

        for x in s_dct:
            if s_dct[x] != t_dct[x]:
                return False
        return True