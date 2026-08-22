class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) +1
            if freq[num] >1:
                return num




            
        