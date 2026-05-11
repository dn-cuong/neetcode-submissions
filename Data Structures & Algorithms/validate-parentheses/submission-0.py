class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "({[":
                stack.append(x)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if x == '}' and top != '{':
                    return False
                if x == ')' and top != '(':
                    return False
                if x == ']' and top != '[':
                    return False
        return True if not stack else False