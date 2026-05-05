class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        sampleSpace = set()

        for num in nums:
            if num in sampleSpace:
                return num
            else:
                sampleSpace.add(num)
        
        