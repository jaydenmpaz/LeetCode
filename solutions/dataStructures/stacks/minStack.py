class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minimum = self.getMin()
        if minimum == None or val < minimum:
            minimum = val
        
        self.stack.append([val, minimum])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()