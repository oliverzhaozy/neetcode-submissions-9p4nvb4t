import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        for t in tokens:
            if t in operators:
                n1, n2 = int(stack.pop()), int(stack.pop())
                product = operators[t](n2, n1)
                stack.append(product)
            else:
                stack.append(t)

        return int(stack[0])