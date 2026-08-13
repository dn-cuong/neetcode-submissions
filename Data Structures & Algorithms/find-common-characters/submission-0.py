class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # use the 26 elements to keep track of frequency of all the word in list -> then loop through the frequency list and then ans += word * (frequency // 2)
        alphabet = [0] * 26

        for word in words:
            for x in word:
                alphabet[ord(x) - ord('a')] += 1
        ans = []
        n = len(words)
        for i in range(len(alphabet)):
            temp = alphabet[i] // n
            while temp > 0:
                ans.append(chr(i+97))
                temp -= 1
        return ans