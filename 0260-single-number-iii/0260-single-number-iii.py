class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor_x = 0

        for num in nums:

            xor_x ^= num

        mask = xor_x & -xor_x

        groupa = groupb = 0

        for num in nums:

            if num & mask:

                groupa ^= num

            else:

                groupb ^= num

        return [groupa , groupb]               
        