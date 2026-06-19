class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        mp = {

            ')' : '(' , 
            ']' :  '[' ,
            '}' : '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)

            else:

                if not stack:
                    return False


                if stack[-1] != mp[ch]:
                    return False

                stack.pop()


        return not stack             







        