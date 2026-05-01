class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maximum = arr[len(arr)-1]

        for i in range(len(arr)-2,-1,-1):

            val = arr[i]
            arr[i] = maximum
            maximum = max(maximum, val)
        
        arr[len(arr)-1] = -1

        return arr