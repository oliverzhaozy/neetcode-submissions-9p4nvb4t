class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = []
        open_brackets = ['(', '{', '[']

        brackets = {')': '(', '}': '{', ']': '['}
            
        for char in s:
            # [()]
            if char in open_brackets:
                open_chars.append(char)
            # Else the char is a close bracket
            else:
                if not open_chars:
                    return False
                if brackets[char] != open_chars[-1]:
                    return False
                else:
                    open_chars.pop()

        if not open_chars:
            return True
        else:
            return False


            
        