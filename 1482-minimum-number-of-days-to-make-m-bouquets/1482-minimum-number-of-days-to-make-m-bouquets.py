class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m* k > len(bloomDay):

            return -1
        low = min(bloomDay)

        high = max(bloomDay)

        while(low<high):

            bouqets = 0
            flowers = 0

            mid= (low+high)//2

            for day in bloomDay:

                if day<=mid:

                    flowers+=1

                    if flowers ==k:
                        bouqets+=1


                        flowers = 0

                else:
                    flowers = 0

            if bouqets >= m:
                high = mid

            else:
                low = mid+1

        return low                             




        