class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        events = [0]*1001

        for passengers , start , end in trips:

            events[start ]+= passengers

            events[end]-= passengers

        current = 0

        for i in range (1001):

            current+= events[i]

            if current > capacity:

                return False

        return True        
