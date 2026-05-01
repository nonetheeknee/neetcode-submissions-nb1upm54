class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums)==0: return 0
        
        pointer = len(nums)
        i = 0
        while nums[pointer-1] == val :
            pointer -= 1
            if pointer==0: break
            

        while i<pointer:

            if nums[i] == val:
                nums[i] = nums[pointer-1]
                nums[pointer-1] = val
                while nums[pointer-1] == val:
                    pointer -= 1
            i+=1
        
        if pointer == -1: return 0 
        else: return len(nums[:pointer])  