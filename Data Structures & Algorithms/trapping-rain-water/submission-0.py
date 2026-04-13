class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[height[0]]*len(height)
        suffix=[height[len(height)-1]]*len(height)
        result=0

        for i in range(1,len(height)):
            prefix[i]=max(prefix[i-1],height[i])
        print(prefix)
        for i in range(len(height)-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i])
        print(suffix)
        
        for i in range(0,len(height)):
            if min(prefix[i],suffix[i])>height[i]:
                result+=min(prefix[i],suffix[i])-height[i]
        return result