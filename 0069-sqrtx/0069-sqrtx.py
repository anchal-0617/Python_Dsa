class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x-1
        if x== 0 or x== 1:
            return x



        while(low<=high):

            mid = (low+high)//2

            if mid*mid == x:
                return mid

            elif mid*mid > x:

                high = mid-1

            else:

                low = mid+1

        return low -1    
                        