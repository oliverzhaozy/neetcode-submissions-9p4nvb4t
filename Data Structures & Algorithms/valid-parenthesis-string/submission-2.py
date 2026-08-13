class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1, stack2 = [], []

        for i, c in enumerate(s):
            if c == '(':
                stack1.append((i, c))
            elif c == '*':
                stack2.append((i, c))
            else: # c == ')'
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False

        if len(stack2) < len(stack1):
            return False
        while stack1:
            i1, c1 = stack1.pop()
            i2, c2 = stack2.pop()
            if i2 < i1:
                return False
        return True