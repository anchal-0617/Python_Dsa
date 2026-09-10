class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = nums[0]
        for i in range (1,len(nums)):
            nums[i] = nums[i] + prefix

            prefix =  nums[i]

        return nums    
        