class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """




        n = len(s)

        t = [[0] * n for _ in range(n)]
        count = 0

        for l in range (1,n+1):
            for i in range (n-l+1):
                j = i+l-1

                if (i==j):
                    t[i][j] = True

                elif ( i+1 == j):
                    t[i][j] = s[i] == s[j]

                else:
                    t[i][j] =  s[i] == s[j] and t[i+1][j-1]

                if t[i][j]:
                    count = count+1

        return count         

        