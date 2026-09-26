class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for b in s:
            # b is an open bracket
            if b not in mapping:
                stack.append(b)
            
            # b is a close bracket
            elif not stack:
                return False
            else:
                if stack[-1] != mapping[b]:
                    return False
                stack.pop()
        
        return False if stack else True

