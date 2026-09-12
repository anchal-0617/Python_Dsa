class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        for i in range(len(nums)):
            count = 0
            while(nums[i]>0):
                


                digit = nums[i] % 10
                count += 1
                
                nums[i] = nums[i]//10
            if count % 2 == 0:
                even+=1    

                
                

        return even

         