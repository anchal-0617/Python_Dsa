class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """


        # top = 0
        # down = len(matrix) -1
        # left = 0
        # right = len(matrix[0]) -1


        # result = []

        # while top <= down and left <= right :
        #     for i in range(left , right + 1):
        #         result.append(matrix[top][i])
        #     top += 1

        #     for i in range(top , down +1):
        #         result.append(matrix[i][right])

        #     right -=1

        #     if top <= down:

        #         for i in range(right , left -1 ,-1):
        #             result.append(matrix[down][i])

        #         down -=1

        #     if left <= right:     


        #         for i in range(down , top -1 , -1):
        #             result.append(matrix[i][left])

        #         left +=1                 
        # return result
        ans = []
        rowS = 0
        colS = 0
        rowE = len(matrix) - 1
        colE = len(matrix[0]) - 1


        while ( rowS <= rowE) and (colS<= colE):

            i = colS
            while(i<=colE):

                ans.append(matrix[rowS][i])

                i+=1
            rowS+=1

            i = rowS

            while(i<=rowE):

                ans.append(matrix[i][colE]) 

                i+=1

            colE-=1


            if (rowS<=rowE):

                i = colE


                while (i>=colS):
                    ans.append(matrix[rowE][i])

                    i-= 1

                rowE-=1


            if(colS<=colE):
                i = rowE
                while(i>=rowS):

                    ans.append(matrix[i][colS])

                    i-=1

                colS+=1

        return ans                    


            


























        