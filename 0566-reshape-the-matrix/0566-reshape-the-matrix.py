class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        m = len(mat)

        n = len(mat[0])

        if m* n != r*c:
            return mat

        ans = []
        temp = []

        for i in range(m):
            for j in range(n):

                temp.append(mat[i][j])

                if len(temp) == c:

                    ans.append(temp)

                    temp = []

        return ans                


        