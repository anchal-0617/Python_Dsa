class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        gola_index  =  -1

        # find breakpt.

        for i in range(n-1 , -1 , -1):
            if nums[i] > nums[i-1]:
                gola_index  = i-1

                break
        # swap

        if gola_index != -1:
            for i in range(n-1 , gola_index , -1):
                if nums[i] > nums[gola_index]:

                    nums[i] , nums[gola_index] = nums[gola_index] , nums[i]

                    break

        nums [gola_index + 1: ] = reversed(nums[gola_index +1:])                    