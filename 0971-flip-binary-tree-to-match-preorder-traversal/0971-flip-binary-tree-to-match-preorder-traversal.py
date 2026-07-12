# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: Optional[TreeNode]
        :type voyage: List[int]
        :rtype: List[int]
        """
        
        self.i = 0

        ans = []

        def solve(root):
            if root is None:
                return True

            if root.val != voyage[self.i]:
                return False

            self.i += 1

            if root.left and root.left.val != voyage[self.i]:

                ans.append(root.val)

                return solve(root.right) and solve(root.left)
            return solve(root.left) and solve(root.right) 

        if solve(root):

            return ans

        return [-1]           

