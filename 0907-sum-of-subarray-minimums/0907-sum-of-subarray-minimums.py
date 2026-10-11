class Solution(object):
    def sumSubarrayMins(self, nums):
        """
        :type arr: List[int]
        :rtype: int
        """
        # here we use concept of next smallest left and right and through that we are fiding the minimum subarrays and one more thing we store indices not the values and in two loops , one we take >= and in other > bcz to overcome the duplicates elements
        n = len(nums)

        nsl = [-1]*n
        nsr = [n]*n

        stack = []

        for i in range(n):

            while stack and nums[stack[-1]]>= nums[i]:

                stack.pop()

            if stack:

                nsl[i] = stack[-1]

            stack.append(i)

        stack = []

        for i in range(n-1,-1,-1):

            while stack and nums[stack[-1]]> nums[i]:

                stack.pop()

            if stack:

                nsr[i] = stack[-1]

            stack.append(i)    

        ans = 0

        MOD = 10 **  9 + 7

        for i in range(n):

            left = i-nsl[i]
            right = nsr[i] - i

            ans = (ans + nums[i] * left * right ) % MOD

        return ans      


        