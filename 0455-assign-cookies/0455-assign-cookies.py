class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g.sort()
        s.sort()
        j = 0
        for i in range(len(g)):
            
            while j < len(s):
                if s[j] >=  g[i]:
                    count +=1 
                    s[j] = 0
                    break

                j+=1

        return count      

        # count = 0
        # g.sort()
        # s.sort()
        # for i in range(len(g)):

        #     for j in range(len(s)):
                

        #         if g[i] <= s[j]:

        #             count +=1 
        #             s[j]= 0
        #             break

        # return count                 
        




























