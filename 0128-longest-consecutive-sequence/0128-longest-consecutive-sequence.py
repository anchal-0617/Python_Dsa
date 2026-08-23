class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums1 = set(nums)

        longest = 0

        for num in nums1:

            if num - 1 not in nums1:

                length = 1

                while num + length in nums1:
                    length += 1

                longest = max(longest , length)    
        return longest             
        