class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(openb, closeb, stack):
            # Base case
            if closeb > openb:
                return
            if openb == n and closeb == n:
                res.append(stack)
                return
            
            if openb < n:
                backtrack(openb + 1, closeb, stack + '(')
            backtrack(openb, closeb + 1, stack + ')')
        
        backtrack(0, 0, "")
        return res

