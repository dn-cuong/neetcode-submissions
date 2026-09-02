class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(idx, s):
            if idx == len(digits):
                res.append(s)
                return

            for char in mapping[digits[idx]]:
                backtracking(idx + 1, s + char)

        backtracking(0, "")
        return res if digits else []