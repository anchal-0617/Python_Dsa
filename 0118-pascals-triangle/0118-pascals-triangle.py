class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ans = []
        n = numRows
        for n in range( n ):
            row = [1]

        
            for i in range(1,n):
                # value = row[-1] * (n-i) // i

                row.append(ans[n-1][i-1]+ ans[n-1][i])

            if n>0: 

                row.append(1)   
            ans.append(row)    
        return ans    
        