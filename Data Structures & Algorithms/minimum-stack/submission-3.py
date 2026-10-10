class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val or val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_val[-1]:
            self.min_val = self.min_val[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
