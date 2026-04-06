class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        if len(s)!=len(t):
            return False
        
        for i in range(0, len(s)):

            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1
            
            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1

        for key in s_freq:
            if key not in t_freq:
                return False

            if s_freq[key] != t_freq[key]:
                return False
        
        return True
