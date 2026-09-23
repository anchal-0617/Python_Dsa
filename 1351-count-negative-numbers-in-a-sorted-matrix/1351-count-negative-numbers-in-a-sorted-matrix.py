class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):

            for j in range(m):

                if grid[i][j]<0:
                    count +=1

        return count            



        