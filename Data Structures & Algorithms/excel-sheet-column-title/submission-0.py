class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res += alphabet[columnNumber % 26]
            columnNumber //= 26

        return res[::-1]