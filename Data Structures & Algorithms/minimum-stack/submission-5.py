class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.lowest = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.lowest = min(self.lowest, val)
        self.minStack.append(self.lowest)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.lowest = self.minStack[-1]
        else:
            self.lowest = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
