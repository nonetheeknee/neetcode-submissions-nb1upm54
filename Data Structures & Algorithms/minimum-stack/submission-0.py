class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack != [] and val>self.minStack[-1]:
            for i,value in enumerate(self.minStack):
                if val>value:
                    self.minStack.insert(i,val)
                    break
        else:
            self.minStack.append(val)

        

    def pop(self) -> None:
        self.minStack.remove(self.stack[-1])
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        
