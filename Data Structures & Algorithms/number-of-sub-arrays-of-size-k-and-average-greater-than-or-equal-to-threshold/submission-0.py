class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        result = 0
        i = 0
        j = k
        sum_val = 0 

        for num in arr[:k]:
            sum_val += num
        
        target = threshold * k
        if sum_val >= target:
            result += 1

        while j < len(arr):
            sum_val = sum_val + arr[j] - arr[i]
            if sum_val >= target:
                result += 1

            i += 1
            j += 1

        return result
