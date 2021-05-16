# Find different ways to make changes of n cents with given set S
# track the no. of ways using a table(dp)
# total no. of ways at a particular cell will be equal to 
# the no. of ways in which you can sum up to the curr_Sum(column)
# 1. by including the curr_element (S[i]) + 2. byb excluding the curr_element  

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp = [[0 for i in range(n+1)]for j in range(m+1)]
        
        for i in range(m):
            dp[i][0]=1
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if S[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-S[i-1]]+dp[i-1][j]
        
        return dp[-1][-1]            

t = int(input())
for _ in range(t):
    n,m = list(map(int, input().strip().split()))
    S = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.count(S,m,n))
