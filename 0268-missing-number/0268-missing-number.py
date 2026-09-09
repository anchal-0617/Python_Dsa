class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        j = 0
        for i in range(len(nums)):

            
            if nums[i] == j:
                
                j+=1
            else:
                return j   

        return j         
        