class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ""
        for ch in s:

            if ch.isalnum():

                result += ch.lower()

        i = 0
        j = len(result)-1
        result.split()

        while(i<j):
            

            if result[i] != result[j]:
                return False

            i+=1

            j-=1
        return True

                


                      

            


        