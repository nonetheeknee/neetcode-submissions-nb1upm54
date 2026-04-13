class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []


        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            j=i+1
            k=len(nums)-1

            while j<k:
                if nums[j]+nums[k]==-nums[i] and [nums[i],nums[j],nums[k]] not in result:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif nums[j]+nums[k]<-nums[i]: 
                    j+=1
                else:
                    k-=1
        return result