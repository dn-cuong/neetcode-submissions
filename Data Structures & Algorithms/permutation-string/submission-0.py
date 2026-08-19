class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

            count1 = [0] * 26
            count2 = [0] * 26

            for c in s1:
                count1[ord(c) - ord('a')] += 1

            k = len(s1)

            # first window
            for i in range(k):
                count2[ord(s2[i]) - ord('a')] += 1

            if count1 == count2:
                return True

            # slide window
            for right in range(k, len(s2)):
                # add new character
                count2[ord(s2[right]) - ord('a')] += 1

                # remove old character
                left = right - k
                count2[ord(s2[left]) - ord('a')] -= 1

                if count1 == count2:
                    return True

            return False