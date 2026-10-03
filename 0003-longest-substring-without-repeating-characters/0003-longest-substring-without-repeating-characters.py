class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        seen = set()
        

        i = 0 
        j=0

        while(j<n):
            if s[j] in seen:
                seen.remove(s[i])
                i+=1

            else:
                seen.add(s[j]) 
                max_len = max(max_len , j-i+1)
                j+=1   

                

        return max_len            




        