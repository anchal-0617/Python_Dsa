class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """


        n = len(mat)
        for i in range(4):

            if mat == target:
                return True

            for row in range(n):
                for col in range(row + 1 , n):

                    mat[row][col] , mat[col][row] = mat[col][row] , mat[row][col]
                    

            for row in range(len(mat)):

                for col in range((len(mat) + 1 )//2):

                    mat[row][col] , mat[row][n-col-1] = mat[row][n-col-1], mat[row][col] 

        return False         


        