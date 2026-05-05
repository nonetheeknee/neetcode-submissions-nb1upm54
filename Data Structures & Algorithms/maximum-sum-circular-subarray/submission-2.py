class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:


        inMax = nums[0]
        currSum = 0
        total = 0

        for num in nums:
            total += num
            currSum += num
            inMax = max(inMax, currSum)
            if currSum < 0 : currSum = 0

        minSum = nums[0]
        sum = 0

        for num in nums:
            sum += num
            if sum - num > 0 and sum - num > sum : sum = num
            minSum = min(minSum, sum)
        
        if total - minSum == 0: return inMax
        else: return max(inMax, total - minSum)




        

        