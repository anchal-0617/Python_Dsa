class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """



        stack = []
        n = len(nums)

        for i in range(n):
            while stack and stack[-1] > nums[i] and (len(stack) -1 + n-i) >= k:
                stack.pop()

            if len(stack) < k :
                stack.append(nums[i])    

        return stack        
        