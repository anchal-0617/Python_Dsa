# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """



        def solve(root , p , q):

            if root == None:
                return None

            if root == p or root == q:
                return root

            left1 = solve(root.left,p,q)

            right1 = solve(root.right, p ,q)

            if left1!= None and right1!= None:
                return root

            if left1!= None:
                return left1

            return right1

        return solve(root,p,q)                   
        