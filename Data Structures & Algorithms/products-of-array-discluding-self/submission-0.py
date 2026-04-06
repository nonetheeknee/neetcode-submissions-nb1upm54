class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        zero_count = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1
        
        for i in range(0, len(nums)):
            if zero_count  > 1:
                output.append(0)
            elif zero_count == 1 and nums[i] != 0:
                output.append(0)
            elif nums[i] == 0:
                output.append(product)
            else:
                output.append(int(product/nums[i]))
        return output
            
           
        