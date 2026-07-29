class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        

        n = len(mat)

        ans = 0

        for i in range (n):

            ans += mat[i][i]

            if i != n-1-i:

                ans += mat[i][n-1-i]
        return ans         