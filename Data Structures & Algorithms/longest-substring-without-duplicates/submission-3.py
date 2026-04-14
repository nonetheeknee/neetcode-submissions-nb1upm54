class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result=0
        start = 0

        map = set()

        for end in range(len(s)):

            while s[end] in map:
                map.remove(s[start])
                start+=1
            
            map.add(s[end])

            result = max(result,end-start+1)
      
        return result               