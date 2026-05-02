class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {')':'(',']':'[','}':'{'}
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            elif stack != [] and pairs.get(ch)==stack[-1]:
                stack.pop()

            else:
                return False
        return stack == []



        