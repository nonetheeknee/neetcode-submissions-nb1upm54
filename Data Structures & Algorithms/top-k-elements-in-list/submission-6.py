class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        bucket = defaultdict(list)
        result = []


        for num in nums:
            freq[num] += 1       

        for num in freq:
            bucket[freq[num]].append(num)

        
        for i in range(len(nums),0,-1):
            if bucket[i]!=0:
                for num in bucket[i]:
                    result.append(int(num))
                    print("result at %i ="%i, result)
                    if len(result)==k:
                        return result      