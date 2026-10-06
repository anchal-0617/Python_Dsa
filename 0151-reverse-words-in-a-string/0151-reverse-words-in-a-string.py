class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()

        #words.reverse()

        r_w = words[::-1]

        

        return ' '.join(r_w)    













            



        