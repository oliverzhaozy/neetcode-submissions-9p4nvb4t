class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz", 
        }

        def backtrack(i, curStr):
            # Base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return 
            
            for c in digit_to_letters[digits[i]]:
                backtrack(i + 1, curStr + c)
            
        backtrack(0, "")
        return res if digits else []
