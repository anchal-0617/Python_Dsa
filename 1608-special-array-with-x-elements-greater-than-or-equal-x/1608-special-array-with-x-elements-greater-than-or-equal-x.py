class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        

        for i in range(1,len(nums)+1):

            count = 0

            for num in nums:

                if num>=i:

                    count +=1

            if count == i:
                return count



        
        return -1            
        