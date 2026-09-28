class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        # rows = len(mat)
        # cols = len(mat[0])

        # for i in range(rows):
        #     for j in range(cols):

        #         top = mat[i-1][j] if i > 0 else float('-inf')
        #         bottom = mat[i+1][j] if i < rows-1 else float('-inf')
        #         left = mat[i][j-1] if j > 0 else float('-inf')
        #         right = mat[i][j+1] if j < cols-1 else float('-inf')

        #         if (mat[i][j] > top and
        #             mat[i][j] > bottom and
        #             mat[i][j] > left and
        #             mat[i][j] > right):

        #             return [i, j]

        rows = len(mat)

        col = len(mat[0])

        low = 0

        high = col - 1

        while(low<=high):

            mid = (low+high)//2

            max_row = 0


            for i in range(rows):

                if mat[i][mid] > mat[max_row][mid]:

                    max_row = i

            curr_element = mat[max_row][mid]       


            leftval = mat[max_row][mid-1] if mid>0 else -1

            rightval = mat[max_row][mid+1] if mid< col-1 else -1


            if rightval < mat[max_row][mid] > leftval:

                return [max_row , mid]

            elif leftval > mat[max_row][mid]:

                high = mid -1

            else:
                low = mid+1    






