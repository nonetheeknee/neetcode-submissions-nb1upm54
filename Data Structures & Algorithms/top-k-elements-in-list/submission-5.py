class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        result = []


        for num in nums:
            freq[num] += 1

        bucket = defaultdict(list)

        for num in freq:
            bucket[freq[num]].append(num)

        print("bucket= ",bucket)
        
        for i in range(len(nums),0,-1):
            if bucket[i]!=0:
                for num in bucket[i]:
                    result.append(int(num))
                    print("result at %i ="%i, result)
                    if len(result)==k:
                        return result      