class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        ans = [1]
        n = rowIndex+1

        for i in range(1,n):
            value = ans[-1] * (n-i) // i

            ans.append(value)

        return ans     
