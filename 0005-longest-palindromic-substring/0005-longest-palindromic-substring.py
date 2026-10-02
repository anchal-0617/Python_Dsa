class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


#         def isCheck(result):

#             i = 0
#             j = len(result)-1
#             while(i<j):
            

#                 if result[i] != result[j]:
#                     return False

#                 i+=1

#                 j-=1
#             return True

#         if len(s) == 1:
#             return s    

#         result = ''

#         for i in range(len(s)):
        
#             ans = ''

#             for j in range(i,len(s)):
        
        

#                 ans+= s[j]

#                 if isCheck(ans):

#                     if len(ans) > len(result):
#                         result = ans


#         return result            

# # to remove TLE we use MID approch


#         def expand(i,j):

#             result = ''

#             while i>0 and j<len(s)-1 and s[i]==s[j]:

#                 i-=1


#                 j+=1

#             return ([i+1,j])


#         for i in range(len(s)):

#             ans = expand(i,i)






#             ans = expand(i+1 , i)     

        n = len(s)
        maxL = 0
        idx = 0

        t = [[0] * n for _ in range(n)]
        count = 0

        for l in range (1,n+1):
            for i in range (n-l+1):
                j = i+l-1
                

                if (i==j):
                    t[i][j] = True
                    
                    maxL = 1

                elif s[i]==s[j] and l==2 :
                    t[i][j] = True
                    maxL = 2
                    idx = i
                elif s[i]==s[j] and t[i+1][j-1]==True:
                    t[i][j]= True  
                    if j-i+1> maxL  :
                        maxL = j-i+1
                        idx = i 



                else:
                    t[i][j]= False

            
        return s[idx:idx+maxL]






               

    
