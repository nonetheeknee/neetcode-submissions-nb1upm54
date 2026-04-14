class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        result = 0
        i,j = 0,0
        pos = -1

        while j in range(len(nums)):
            if nums[j]==0:
                if pos<i:
                    pos=j                
                else:
                    i=pos+1
                    pos=j
            result=max(result,j-i+1)
            j+=1
        return result