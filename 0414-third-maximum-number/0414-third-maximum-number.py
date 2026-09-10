class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        n = len(nums)
        nums.sort()
        if n>=3:
            return (nums[n-3])
        else:
            return (nums[n-1])    
        