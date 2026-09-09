class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        n = len(nums)
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1

            if freq[nums[i]] >= 2:
                return True
        
        return False    

        