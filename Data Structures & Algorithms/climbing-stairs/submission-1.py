class Solution:
    def climbStairs(self, n: int) -> int:

        memo = defaultdict(int)

        for i in range(1,n+1):

            if i<=2 :
                memo[i] = i
            else: 
                memo[i]= memo[i-1]+memo[i-2]
        
        return memo[n]
            
