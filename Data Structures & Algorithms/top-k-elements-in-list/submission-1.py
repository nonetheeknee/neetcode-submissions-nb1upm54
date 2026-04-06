class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        freq = {}
        count = {}

        for i in range(0, len(nums)):
            count[i+1] = []
            if nums[i] in freq.keys():
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        print(freq)
        print(count)

        for key in freq.keys():
            count[freq[key]].append(key)

        for i in range(0, len(nums)):
            if len(nums)-i != 0:
                if len(count[len(nums)-i])!=0:
                    for j in range (0,len(count[len(nums)-i])):
                        result.append(count[len(nums)-i][j])
                        if len(result)==k:
                            return result