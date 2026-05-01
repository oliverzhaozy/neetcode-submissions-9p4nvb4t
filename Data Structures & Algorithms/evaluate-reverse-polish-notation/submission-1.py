import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                res = ops[token](stack[-2], stack[-1])
                for _ in range(2):
                    stack.pop()
                stack.append(res)

        return int(stack[0])
