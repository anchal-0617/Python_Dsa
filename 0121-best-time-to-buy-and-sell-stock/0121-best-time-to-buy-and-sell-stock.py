class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # mini = prices[0]
        # maxi = 0
        # # we keep a mini

        # for i in range(len(prices)):

        #     sub = prices[i] - mini

        #     maxi = max(maxi , sub)

        #     mini = min(mini ,prices[i])

        # return maxi    
        # n = len(prices)
        # max_profit = 0

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)

        # return max_profit     

        minprice = float('inf')
        maxprofit = 0
        n = len(prices)

        for i in range(n):
            minprice = min(minprice , prices[i])

            profit = prices[i] - minprice
            maxprofit = max(maxprofit , profit) 
        return maxprofit        