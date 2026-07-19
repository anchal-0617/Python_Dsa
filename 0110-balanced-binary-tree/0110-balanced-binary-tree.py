# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def height(self , root):
        if not root:
            return 0
        leftH =  self.height(root.left)
        rightH = self.height(root.right)
        return max(leftH , rightH) + 1

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # def dfs(root):
        #     if root is None:
        #         return 0

        #     left = dfs(root.left)
        #     if left == -1:
        #         return -1
        #     right = dfs(root.right)
        #     if right == -1:
        #         return -1

        #     if abs(left-right) >1:
        #         return -1


        #     height = 1 + max(left, right)
        #     return height

        # return dfs(root)!= -1
        def solve(root):
            if not root:
                return True

            leftH = self.height(root.left)

            rightH = self.height(root.right)

            if abs(leftH - rightH) > 1:
                return False

            return solve(root.left) and solve(root.right)

        return solve(root)     
        

