class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        t = [[0] * n for _ in range(n)]
       

        for l in range (1,n+1):
            for i in range (n-l+1):
                j = i+l-1

                if (i==j):
                    t[i][j] = True

                elif ( i+1 == j):
                    t[i][j] = s[i] == s[j]

                else:
                    t[i][j] =  s[i] == s[j] and t[i+1][j-1]

        dp = [0] * n
        for i in range(n):
            if t[0][i] == True:
                dp[i] = 0
            else:

                dp[i] = float('inf')
                for k in range(i):

                    if(t[k+1][i] == True and dp[i] > 1+dp[k]):
                        dp[i] = 1+dp[k]



        return dp[n-1]                


        