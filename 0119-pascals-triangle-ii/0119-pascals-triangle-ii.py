class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        # ans = [1]
        # n = rowIndex + 1

        # for i in range(1,n):
        #     value = ans[-1] * (n-i) // i

        #     ans.append(value)

        # return ans     

        ans = []
        n = rowIndex + 1
        for n in range( n ):
            row = [1]

        
            for i in range(1,n):
                # value = row[-1] * (n-i) // i

                row.append(ans[n-1][i-1]+ ans[n-1][i])

            if n>0: 

                row.append(1)   
            ans.append(row)    
        return ans[-1] 
