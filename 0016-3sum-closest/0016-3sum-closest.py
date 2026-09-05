class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n= len(nums)
        closest = float("inf")

        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,len(nums)):


        #             sum = nums[i] + nums[j] +nums[k]

        #             if abs(target - sum) < abs(target - closest): 
        #                 closest = sum

        # return closest   
        nums.sort()  

        for i in range(n-2):

            left = i+1
            right = n-1

            while left < right :
                sum = nums[i] + nums[left] + nums[right]

                if abs(target - sum) < abs(target - closest):
                    closest = sum

                if (sum < target):
                    left += 1
                else :
                    right -= 1       
        return closest          



        