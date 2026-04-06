class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        check = 0

        for num in nums:
            if num in count:
                count[num] = count[num] + 1
                return True
        
            else:
                count[num] = 1

        return False
        
         