class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        for num in nums:
            if target in nums:

                return True

        return False        
        