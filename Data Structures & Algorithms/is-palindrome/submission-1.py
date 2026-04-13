class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for ch in s:
            if ord(ch) in range(97,122) or ord(ch) in range(65,90) or ord(ch) in range(48,57):
                word+= ch.upper()
        for i in range(0, len(word)):
            print("1:",word[i]," ",word[len(word)-1-i])    
            if word[i]!=word[len(word)-1-i]:
                print("2:",word[i]," ",word[len(word)-1-i])
                return False
        return True
        