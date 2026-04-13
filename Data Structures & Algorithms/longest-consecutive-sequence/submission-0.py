class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seqs = defaultdict(list)
        max_length = 0
        i = 0

        for num in nums:
            seqs[i].append(num)

            while(num+1) in nums:
                seqs[i].append(num+1)
                num+=1
            
            max_length = max(max_length,len(seqs[i]))
            i+=1
        return max_length
        