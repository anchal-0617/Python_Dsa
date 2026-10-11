class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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


        ans1 = 0

        MOD = 10 **  9 + 7

        for i in range(n):

            left = i-nsl[i]
            right = nsr[i] - i

            ans1 = ans1 + nums[i] * left * right 

           

        

        ngl = [-1]*n
        ngr = [n]*n

        stack = []

        for i in range(n):

            while stack and nums[stack[-1]] <= nums[i]:

                stack.pop()

            if stack:

                ngl[i] = stack[-1]

            stack.append(i)

        stack = []

        for i in range(n-1,-1,-1):

            while stack and nums[stack[-1]]< nums[i]:

                stack.pop()

            if stack:

                ngr[i] = stack[-1]

            stack.append(i)   


        ans = 0

        MOD = 10 **  9 + 7

        for i in range(n):

            left = i-ngl[i]
            right = ngr[i] - i

            ans = ans + nums[i] * left * right 


        return ans - ans1    

           

         

        