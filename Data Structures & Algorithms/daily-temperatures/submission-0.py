class Solution:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
    def pop(self):
        val = self.stack[-1]
        self.stack.remove(self.stack[-1])
        return val

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # the idea is to stack the temperatures and their idices 
        #onto the the stack if they are lesser than the top of stack. 
        # if the temp is higher, pop the stack until a higher temp is found in
        # the stack or the stack is empty. when popping the stack populate the 
        #result array at popping index with the difference between current index 
        #popping index. 

        #self.push((temperatures[0], 0))
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):

            while self.stack and temp > self.stack[-1][0]:
                val = self.pop()
                result[val[1]] = i - val[1]

            self.push([temp,i])
        
        return result


