class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # i=0
        # while(i<len(nums)-1):


        #     if nums[i] == nums[i+1]:
                
        #         i+=2
        #     else:
        #         return nums[i]   

        if len(nums)==1:
            return nums[0]
        if nums[0] < nums[1]:
            return nums[0]
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return nums[len(nums)-1]       
                

        low = 1
        high = len(nums) - 2

        while(low<=high):
            mid = (low+high)//2

            if nums[mid-1]<nums[mid] <nums[mid+1]:

                return nums[mid]
            elif (mid%2 == 0 and nums[mid+1]== nums[mid]) or (mid%2 != 0 and nums[mid-1] == nums[mid] ):
                low = mid+1

            else:
                high = mid-1

                     


        