class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            print("1")
            return False
        
        dict_s = {}
        dict_t = {}

        for i in range(0,len(s)):

            if s[i] in dict_s:
                dict_s[s[i]] = dict_s[s[i]] + 1
            else: 
                dict_s[s[i]] = 1

            if t[i] in dict_t:
                dict_t[t[i]] = dict_t[t[i]] + 1
            else: 
                dict_t[t[i]] = 1
        
        print("dict_t", dict_t)
        print("dict_s", dict_s)

        for key in dict_s.keys():
            if key in dict_t:
                if dict_s[key] != dict_t[key]:
                    print("log: ",key, " ", dict_s[key], " ", dict_t[key])
                    return False
            else:
                return False
        
        return True
