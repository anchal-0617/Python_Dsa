# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def solve(left,right):
            

            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:

                return False
            if not root:
                return True   


            left1 = solve(left.left , right.right)
            right2 = solve(left.right , right.left)

            return left1 and right2

        return solve(root.left  , root.right)
                      
