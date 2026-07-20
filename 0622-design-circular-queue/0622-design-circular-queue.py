class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """

        self.q = [0]*k
        self.front = 0
        self.rear = -1
        self.curr_count = 0
        self.capacity = k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.curr_count += 1
        return True  

        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.front = (self.front + 1 ) % self.capacity 
        
        self.curr_count -= 1
        return True


        

    def Front(self):
        """
        :rtype: int
        """

        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """

        if self.curr_count == 0:
            return True
        return False    
        

    def isFull(self):
        """
        :rtype: bool
        """

        if self.curr_count == self.capacity:
            return True
        return False    

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()