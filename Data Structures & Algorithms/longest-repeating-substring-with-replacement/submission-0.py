class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 1
        

        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for i in range(0,len(s)):
                length = 0
                rep = 0

                for j in range(i,len(s)):
                    if s[j]==char:
                        length+=1
                    
                    else: 
                        rep +=1
                        if rep>k: break
                        else:
                            length+=1
                result = max(result, length)
                   
            
            
        return result     