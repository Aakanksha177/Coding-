# we can solve this question with similar approach that we used to find longest common
# subsequence by creating another array and sorting it then comparing it with the initial array
# and the resultant common subsequence will be the longest increasing sunsequences

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        
        b=sorted(list(set(a)))
        m=len(b)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(n+1):
                
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

for _ in range(int(input())):
    n = int(input())
    a = [ int(x) for x in input().split() ]
    ob=Solution()
    print(ob.longestSubsequence(a,n))