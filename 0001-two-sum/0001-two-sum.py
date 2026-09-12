class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # for i in range(len(nums)):

        #     complement = target - nums[i]

        #     if complement in nums and nums.index(complement) != i: 
        #         return(i,nums.index(complement))


        # mp = {}

        # for i in range(len(nums)):

        #     complement = target - nums[i]

        #     if complement in mp:
        #         return [mp[complement] , i]

        #     mp[nums[i]] = i    


        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):

                if nums[i] + nums[j] ==target:

                    return (i,j)