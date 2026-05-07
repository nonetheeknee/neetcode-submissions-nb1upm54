class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = []
        curr = 0

        for num in nums:
            prefix_sum.append(curr)
            curr += num

        total_sum = curr
        for i,prefix in enumerate(prefix_sum):
            if prefix == total_sum - prefix - nums[i]: 
                return i

        return -1
