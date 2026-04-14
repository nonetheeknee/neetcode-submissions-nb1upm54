class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k==0: return False

        i = 0
        j=0
        window = set()

        while j in range(len(nums)) and j<=i+k+1:
            if nums[j] in window:
                return True
            else:
                window.add(nums[j])
                j+=1

            if j==i+k+1:
                window.remove(nums[i])
                i+=1

        return False
