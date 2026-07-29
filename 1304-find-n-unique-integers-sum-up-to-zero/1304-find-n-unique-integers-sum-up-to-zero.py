class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        start = 1
        result = [0]*n
        i = 0
        while (i+1 <n):

            result[i] = start

            result[i+1] = - start

            i+=2
            start +=1
        return result 
        