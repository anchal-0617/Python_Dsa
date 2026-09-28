class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        if not matrix :
            return False
        rows =  len(matrix)
        cols = len(matrix[0])


        left  , right = 0 , rows * cols - 1

        while left <=right:
            mid = (left+right) // 2

            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True

            elif value > target:
                right = mid -1

            else:
                left = mid +1
        return False                    

        