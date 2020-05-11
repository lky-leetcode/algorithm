class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(x)
        else:
            top = self.minStack[len(self.minStack) - 1]
            self.minStack.append(top)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()


    def top(self) -> int:
        if len(self.stack):
            return self.stack[len(self.stack) - 1]
        return None
    
    def getMin(self) -> int:
        if len(self.minStack):
            return self.minStack[len(self.minStack) - 1]
        return None
