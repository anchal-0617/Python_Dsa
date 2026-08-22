class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        n = numRows
        for n in range(1 , n +1):
            row = [1]

        
            for i in range(1,n):
                value = row[-1] * (n-i) // i

                row.append(value)
            ans.append(row)    
        return ans    
        