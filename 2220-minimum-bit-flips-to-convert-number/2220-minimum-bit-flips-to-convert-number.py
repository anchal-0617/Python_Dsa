class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        n = start ^ goal

        count = 0

        while n:

            count += n&1

            n>>=1

        return count    

        
        