class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_sum = float('-inf')
        for i in range(len(accounts)):
        

            

            summ = sum(accounts[i])

            max_sum = max(max_sum , summ)

        return max_sum    

                

        