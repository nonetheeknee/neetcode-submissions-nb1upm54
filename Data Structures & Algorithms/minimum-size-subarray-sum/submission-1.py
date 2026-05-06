class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        i = 0
        j = 0
        result = len(nums)+1

        while j<len(nums):
            summ+=nums[j]

            if summ>=target:
                result = min(result, j-i+1)

                while i<j :
                    summ -=nums[i]
                    i += 1
                    if summ>=target:
                        result = min(result,j-i+1)
                    else:
                        break
            j+=1
        
        return result if result<len(nums)+1 else 0


            
        