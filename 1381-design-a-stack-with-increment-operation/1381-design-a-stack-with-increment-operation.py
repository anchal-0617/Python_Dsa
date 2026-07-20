class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.max_size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)
        

    def pop(self):
        """
        :rtype: int
        """

        if not self.stack:
            return -1

        i = len(self.stack) - 1
        if i > 0:

            self.inc[i-1] += self.inc[i]
        return self.stack.pop() + self.inc.pop()        
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int



        :rtype: None
        """


        idx = min(k , len(self.stack)) - 1

        if idx >= 0:
            self.inc[idx] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)