class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        

    def getMin(self) -> int:
        min_val = self.stack[0]
        for i in self.stack:
            min_val = min(min_val, i)
        return min_val
