class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        t = [[0]*n for _ in range(n)]
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i+l-1

                if s[i] == s[j]:
                    t[i][j] = t[i+1][j-1]
                else:
                    t[i][j] = 1 + min(t[i][j-1] , t[i+1][j])
        return t[0][n-1]                    