# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):

        self.ans = float('-inf')
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def solve(root):
            if root is None:
                return 0

            left1 = max(0 , solve(root.left))

            right1 = max(0 , solve(root.right))

            self.ans = max(self.ans, left1 + right1 + root.val)

            return root.val + max(left1  , right1 ) 

        solve(root)

        return self.ans         