class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        n = len(nums)

        ans = [-1]*n

        stack = []

        for i in range(2 * len(nums)):
            idx = i%n

            while stack and nums[idx] > nums[stack[-1]]:

                j = stack.pop()


                ans[j] = nums[idx]

            if i<n: 
                # we will save in stack index here , so that while pushing in ans we came to know which index we have to update



                stack.append(idx)

        return ans        

                
