class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #we can use the 2 pointer approach here, p1 at index 0 
        # and p2 at index 1. Increment p2 while nums[p1]==nums[p2]
        
        p1 = 0
        p2 = 1

        while p2<len(nums):

            while p2<len(nums) and nums[p1]==nums[p2]: 
                p2+=1
            
            if p2 < len(nums):
                p1+=1
                nums[p1]=nums[p2]
                p2+= 1


        return p1+1