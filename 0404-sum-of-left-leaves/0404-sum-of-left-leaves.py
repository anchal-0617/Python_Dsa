# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        
        def solve(root):
            ans = 0
            if not root:
                return 0

            if root.left and not root.left.left and not root.left.right:
                
                ans += root.left.val

                

            ans += solve(root.left)

            ans += solve(root.right)  

            return ans

        return solve(root)


        