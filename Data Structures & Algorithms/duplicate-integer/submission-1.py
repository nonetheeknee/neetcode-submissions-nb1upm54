class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                map[num] = map[num]+1
                return True
            else:
                map[num] = 1
        return False        