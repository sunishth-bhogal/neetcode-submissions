class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")",
                    "[" : "]", 
                    "{" : "}"}
        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else: 
                if not stack:
                    return False
                if brackets[stack[-1]] != bracket:
                    return False
                stack.pop()
        return not stack
               
