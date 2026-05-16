class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_size = 0
        
        for index, height in enumerate(heights):

            start,end = 0, len(heights)-1

            for i in range(0,index):
                if heights[i]<height:
                    start = i+1
            
            for i in range(index,len(heights)):    
                if heights[i]<height:
                    end = i-1
                    break
            print(index,height,start,end, height*(end-start+1))
            size = height*(end-start+1)
            max_size = max(max_size, height*(end-start+1))
        
        return max_size
                

            



        