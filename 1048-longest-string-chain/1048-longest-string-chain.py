class Solution(object):



    def isPre(self,a,b):
        if len(b)-len(a)!=1:
            return False

        notF = 0
        i=0
        j=0

        while(i<len(a) and j<len(b)):
            if a[i] == b[j]:
                i+=1
            else:
                notF+= 1
                if notF>1:
                    return False
            j+=1     
        return True               
    def longestStrChain(self, words):


        words.sort(key=len)
        n = len(words)
        

        
        maxLis = 1
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if self.isPre(words[j],words[i]):
                    dp[i] = max(dp[i] , dp[j] + 1)
            maxLis = max(maxLis,dp[i])

        return maxLis            