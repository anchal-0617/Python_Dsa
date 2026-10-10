import math
class Solution(object):


    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        low = 1
        high = max(nums)

        while(low<high):

            mid = (low+high) // 2
            add = 0

            for i in nums:

                add+= (i+mid-1)//mid

            if add <= threshold:

                high = mid

            else:
                low = mid+1

        return low                
        