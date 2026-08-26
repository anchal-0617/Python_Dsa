class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        


        mp1 = {}
        mp2 = {}

        for i in range(len(s)):

            if s[i] in mp1 and mp1[s[i]]!= t[i]:
                return False

            if t[i] in mp2 and  mp2[t[i]]!= s[i]:
                return False

            mp1[s[i]] = t[i]

            mp2[t[i]] = s[i]      

        return True      


