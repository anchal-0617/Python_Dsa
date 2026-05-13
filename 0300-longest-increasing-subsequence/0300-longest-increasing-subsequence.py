class Solution(object):
    def lengthOfLIS(self, nums):
        n =len(nums)
        maxLIS = 1
        
        dp = [1] * n 
        for i in range (n):

            for j in range(0,i):

                if nums[j] < nums[i]:

                    dp[i] = max(dp[i] , (dp[j] + 1))

                    maxLIS = max(maxLIS , dp[i])

        return  maxLIS     




        