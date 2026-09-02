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
        def backtracking(start, idx, s):
            if start == len(digits):
                res.append(s)
                return

            for i in range(len(mapping[digits[idx]])):
                backtracking(start+1, idx+1, s + mapping[digits[idx]][i])




        backtracking(0, 0, "")
        return res if digits else []