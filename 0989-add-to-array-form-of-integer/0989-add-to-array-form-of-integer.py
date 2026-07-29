class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        i = len(num) -1

        carry = 0
        ans = []

        while i >= 0 or k > 0 or carry:

            digit = carry

            if i>= 0:

                digit += num[i]

                i-=1
            digit += k%10

            k//=10   
            ans.append(digit%10)
            carry = digit//10

        return ans[::-1]     
        