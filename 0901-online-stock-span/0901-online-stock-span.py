class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        
    #  we are manitaining both prices and span here , so that whenever we pop the stock price , we never loose the span of the popped one as this condn can occur the pop  one required in future so thatss how we sort tid problem and ya thats done!
        
        
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        self.stack.append((price,span))
        
        
        return span
        


