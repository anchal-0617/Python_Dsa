class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        count = 0
        for ch in s:
            if ch in '(' :
                count +=1

            elif ch in ')':

                count -=1
            else:
                continue


            max_count = max(max_count  , count)

        return max_count                
        