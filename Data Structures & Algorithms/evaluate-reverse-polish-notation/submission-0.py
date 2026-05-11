class Solution:
    
    def __init__(self):
        self.stack = []
    
    def pop(self):
        last = self.stack[-1]
        self.stack.pop()
        return last

    def push(self, val):
        self.stack.append(val)

    def evalRPN(self, tokens: List[str]) -> int:

        for op in tokens:

            if op in ('+','-','/','*'):
                val1 = self.pop()
                val2 = self.pop()
                if op == '+':
                    self.push(val1+val2)
                elif op == '-':
                    self.push(val2-val1)
                elif op == '/':
                    self.push(int(val2/val1))
                else:
                    self.push(val1*val2)
            
            else:
                self.push(int(op))
        
        return self.pop()