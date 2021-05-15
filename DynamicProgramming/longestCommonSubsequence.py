class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        # create a 2d matrix with no. of rows = len(s1) i.e., x
        # and no. of columns = len(s2) i.e., y
        dp = [[0 for i in range(y+1)] for j in range(x+1)]
        
        for i in range(1,x+1):
            for j in range(1,y+1):
                # we compare each char of s1 with each char of s2
                # if both are equal then,
                #  we increment the len of substring without this char by 1
                
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1

                # if the char is not equal then we compare the lengths of substring
                # we get by exucluding the char first from s1 and then from s2 and store the max out of those
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[x][y]
    
test_cases = int(input())
for cases in range(test_cases):
    x,y = map(int,input().strip().split())
    s1 = str(input())
    s2 = str(input())
    ob=Solution()
    print(ob.lcs(x,y,s1,s2))