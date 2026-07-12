class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1

        roots = preorder.split(",")

        for i in roots:

            slots -= 1

            if slots < 0:
                return False

            if i != "#" :
                slots += 2

        return slots == 0            
        