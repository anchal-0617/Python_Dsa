# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = 0
        def solve(root):
            
            
            if root is None:
                return 0

            left = solve(root.left)

            right = solve(root.right)

            if root.left and root.left.val != root.val:
                left = 0
            if root.right and root.right.val != root.val:
                right = 0

            self.maxi = max(left+right , self.maxi)    

            return max(left,right) + 1  

        solve(root)   
        return self.maxi            
        