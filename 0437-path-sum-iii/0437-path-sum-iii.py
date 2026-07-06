# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.count = 0

        def path(root,curr_sum):
            if not root:

                return

            curr_sum += root.val

            if curr_sum == targetSum:
                self.count += 1

            path(root.left , curr_sum)

            path(root.right, curr_sum)

        def solve(root):
            if not root:
                return

            path(root,0)

            solve(root.left)

            solve(root.right)    

        solve(root)
        return self.count                

       


        