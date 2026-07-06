# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self,root):

        if not root:
            return 0
        left_sum = self.solve(root.left)

        right_sum = self.solve(root.right)

        self.totalsum = root.val + left_sum + right_sum

        return self.totalsum

    def subtre(self,root):
        
        if not root:
            return 0

        left_sum = self.subtre(root.left)

        right_sum = self.subtre(root.right)   

        subtree_sum = root.val + left_sum + right_sum

        remaining_sum = self.totalsum - subtree_sum
        self.maxP = max(self.maxP , subtree_sum * remaining_sum)
        return subtree_sum      

            

    MOD = 10 ** 9 + 7

    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0


        
        self.maxP = 0
        totalsum = self.solve(root)
        self.subtre(root)

        return self.maxP%self.MOD     