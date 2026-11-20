class Solution:
    def minLength(self, s: str) -> int:
        pairs = {"B" : "A",
                "D": "C"}
        stack = []

        for c in s:
            if stack and c in pairs and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack)

