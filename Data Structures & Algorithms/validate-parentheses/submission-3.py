class Solution:
    def isValid(self, s: str) -> bool:
        open_chars = []
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        for character in s:
            for i, char in enumerate(open_brackets):
                if character == char:
                    open_chars.append(i)
            for j, char in enumerate(close_brackets):
                if character == char:
                    if open_chars == []:
                        return False
                    if open_chars[-1] == j:
                        x = open_chars.pop()
                    else:
                        return False
        if open_chars == []:
            return True
        else:
            return False

    

        