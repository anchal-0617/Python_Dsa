class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        i = -1
        for j in range (len(s)):
            
            if i>= 0 and ((s[i] == 'A' and s[j] == 'B') or (s[i]== 'C' and s[j]== 'D')):
                i-=1
            else :
                i+=1
                s[i] = s[j]        
            

        return i+1  
        