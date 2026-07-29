class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # matrix = [[0] * n for _ in range(m)]

        # for r , c in indices:

        #     for j in range(n):

        #         matrix[r][j] += 1
                
        #     for i in range(m):

        #         matrix[i][c] += 1

        # count = 0

        # for i in range(m):
        #     for j in range(n):

        #         if matrix[i][j] %2 == 1:
        #             count +=1
        # return count    

        #Instead of making matrix we directly count,

        row = [0]*m
        col = [0]*n
        for r,c in indices :
            row[r] +=1

            col[c] +=1

        count = 0

        for i in range(m):
            for j in range(n):

                if (row[i] + col[j]) %2 == 1:
                    count+=1

        return count                




        