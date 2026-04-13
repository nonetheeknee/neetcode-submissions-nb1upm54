class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i, char in enumerate(strs[0]):
            prefix+=char
            for s in strs:
                if i >= len(s) or prefix != s[0:len(prefix)]:
                   
                    return prefix[0:len(prefix)-1]
            
        return prefix