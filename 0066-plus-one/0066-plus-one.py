class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)

        # for i in range(n-1 , -1 , -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     digits[i] = 0
        # return [1] + digits
        num = 0
        for i in range(n):
            
            digit = int(digits[i])

            num = num * 10 + digit
        num += 1    
        arr = []
        while num > 0:
            digit = num % 10

            arr.append(digit)
            num //= 10
        arr.reverse()

        return arr    




        