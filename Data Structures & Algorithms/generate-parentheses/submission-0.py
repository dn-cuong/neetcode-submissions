class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        # keep track of open and close parentheses
        def backtracking(open, close, s):
            if open == 0 and close == 0:
                res.append(s)
                return
            
            # allow to append "(" when the number of "(" is larger than 0
            if open > 0:
                backtracking(open - 1, close, s + "(")

            # allow to append ")" when the remaining ) is larger than (
            if close > open:
                backtracking(open, close - 1, s + ")")

        backtracking(n - 1, n, "(")
        return res