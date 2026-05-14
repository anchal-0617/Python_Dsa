class Solution(object):
    def findLongestChain(self, pairs):

        pairs.sort(key = lambda x: x[1])
        maxLis = 1
        n = len(pairs)
        dp = [1] * n

        for i in range(n):
            for j in range(i):

                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxLis = max(maxLis , dp[i])

        return maxLis            