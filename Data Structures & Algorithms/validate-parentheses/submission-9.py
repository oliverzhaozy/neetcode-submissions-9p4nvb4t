class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = []
        for char in s:
            if char in ['(', '{', '[']:
                open_chars.append(char)
            else:
                if not open_chars:
                    return False
                elif char == ')' and open_chars[-1] == '(':
                    open_chars.pop()
                elif char == '}' and open_chars[-1] == '{':
                    open_chars.pop()
                elif char == ']' and open_chars[-1] == '[':
                    open_chars.pop()
                else:
                    open_chars.append(char)
        if not open_chars:
            return True
        else:
            return False