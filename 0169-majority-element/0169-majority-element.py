class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        n = len(nums)
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1

            if freq[nums[i]] > n//2:
                return nums[i]

        