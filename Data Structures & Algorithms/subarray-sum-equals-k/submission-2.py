class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_diff = {0:1}
        curr_sum = 0
        result = 0


        for num in nums:
            curr_sum += num
            
            result += prefix_diff.get(curr_sum-k, 0)
            prefix_diff[curr_sum] = prefix_diff.get(curr_sum, 0)+1
        
        return result



        