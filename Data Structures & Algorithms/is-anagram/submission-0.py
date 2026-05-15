from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Counter = Counter(s)
        t_Counter = Counter(t)

        for x in s:
            if s_Counter[x] != t_Counter[x]:
                return False
        return True