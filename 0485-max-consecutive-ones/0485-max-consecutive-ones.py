class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcount = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 1:

                count +=1

            else:
                count = 0

            maxcount = max(maxcount , count) 

        return maxcount           
            