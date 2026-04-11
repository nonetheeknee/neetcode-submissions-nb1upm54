class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        result = []


        for num in nums:
            freq[num] += 1
        
        sorted_freq = sorted([count for count in freq.values()],reverse=True)
        print("sorted freq",sorted_freq)
        sorted_freq = sorted_freq[:k]
        print("top k freq",sorted_freq)
        

        for key in freq:
            if freq[key] in sorted_freq:
                result.append(key)
        
        return result


        