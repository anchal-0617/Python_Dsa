class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        low = max(weights)
        high = sum(weights)

        while(low<high):

            mid = (low+high)//2


            required= 1
            current_weight =  0

            for weight in weights:

                if current_weight + weight > mid:
                    required +=1

                    current_weight = 0

                current_weight+= weight

            if required <= days:
                high = mid

            else:

                low = mid+1

        return low                     
        