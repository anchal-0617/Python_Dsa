class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
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

        ans = []

        def dfs(start,path):
            if start == n:
                ans.append(path[:])
                return

            for end in range(start,n):
                if t[start][end]:
                    path.append(s[start:end +1])
                    dfs(end+1,path)
                    path.pop()

        dfs(0,[])
        return ans        

