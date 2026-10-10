class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        for num in nums:

            ones = (ones^num) & ~twos

            twos = (twos^num) & ~ones

        return ones

        #(we use this , to remove twos value from ones thats why we use &~twos and ones there)    

            