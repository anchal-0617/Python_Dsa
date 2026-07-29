class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(matrix)
        n = len(matrix[0])

        rminmax = float('-inf')
        for row in range (m):
            rmin = float('inf')
            for col in range (n):
                rmin = min(rmin , matrix[row][col])
            rminmax = max(rminmax , rmin)

        cminmax = float('inf')
        for col in range (n):
            cmax = float('-inf')
            for row in range (m):
                cmax = max(cmax , matrix[row][col])
            cminmax = min(cminmax , cmax) 


        if rminmax == cminmax:
            return [rminmax]

        return []           
