# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def solve(root,summ):
            
            if not root:
                return False

            summ += root.val

            if not root.left and not root.right:
                return summ == targetSum

            left = solve(root.left,summ)

            right = solve(root.right,summ)


            return left or right

        return solve(root,0)    

            
        