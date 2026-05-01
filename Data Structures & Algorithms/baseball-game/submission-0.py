class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for i in range(0,len(operations)):
            if operations[i]=="D":
                record.append(2*record[-1])
            elif operations[i]=="C":
                record.pop()
            elif operations[i]=="+":
                record.append(record[-1]+record[-2])
            else:
                record.append(int(operations[i]))
        
        return sum(record)
                    
            

        
        