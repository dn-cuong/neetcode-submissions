class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alphabet = [float('inf')] * 26

        for word in words:
            freq = [0] * 26

            for x in word:
                freq[ord(x) - ord('a')] += 1

            for i in range(26):
                alphabet[i] = min(alphabet[i], freq[i])

        ans = []

        for i in range(26):
            for _ in range(alphabet[i]):
                ans.append(chr(i + ord('a')))

        return ans