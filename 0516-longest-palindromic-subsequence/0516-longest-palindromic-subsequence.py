class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        maxL = 0
        idx = 0

        t = [[0] * n for _ in range(n)]
        count = 0

        for l in range (1,n+1):
            for i in range (n-l+1):
                j = i+l-1
                

                if (i==j):
                    t[i][j] = 1
                    
                    

                elif s[i]==s[j] :
                    t[i][j] = 2 + t[i+1][j-1]
                    
                else:
                    t[i][j] = max(t[i][j-1] , t[i+1][j])



                
            
        return t[0][n-1]
        