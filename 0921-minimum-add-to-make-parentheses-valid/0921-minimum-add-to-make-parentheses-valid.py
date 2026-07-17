class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
   

       
       #using stack 
        # stack = []

        # for ch in s:

        #     if stack and stack[-1] == '(' and ch == ')':
        #         stack.pop()
        #     else:
        #         stack.append(ch)

        # return len(stack)

        #Without Stack

        size = 0
        open = 0

        for ch in s:
            if ch == "(" :
                open += 1

            elif (open > 0):
                open -= 1

            else:
                size +=1

        return open + size                
