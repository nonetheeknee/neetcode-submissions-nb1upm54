class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res_set = []
        
        while len(strs) > 0:
            s1 = strs[0]
            subset = [s1]
            f1 = {}
            for char in s1:
                if char in f1:
                    f1[char] += 1
                else: 
                    f1[char] = 1
            
            i = 1
            while i < len(strs):
                s2 = strs[i]
                f2 = {}
                for char in s2:
                    if char in f2:
                        f2[char] += 1
                    else:
                        f2[char] = 1
                
                if f1 == f2:
                    subset.append(strs.pop(i))
                else:
                    i += 1
            res_set.append(subset)
            strs.pop(0)
        return res_set