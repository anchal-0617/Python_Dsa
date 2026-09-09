class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # wrong approch
        # n = len(nums)
        # if n == 1:
        #     return nums
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         j = i
        #         while(j<n-1):
        #             nums[j] = nums[j+1]
        #             j+=1

        #         nums[n-1] = 0 
        #     else:
        #         j+=1       
        
        # return nums     

            #right approch
        j = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[i] , nums[j] = nums[j],nums[i]

                j+=1
        return nums        
                  
        