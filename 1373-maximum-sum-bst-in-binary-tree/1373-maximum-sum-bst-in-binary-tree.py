# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def solve(root):

            if root is None:
                return (True , float('inf') , float('-inf'),0)

            leftBst , left_min , left_max , leftsum = solve(root.left)

            rightBst , right_min , right_max , rightsum = solve(root.right)

            if(leftBst and rightBst and left_max < root.val < right_min):

                current_sum = leftsum + rightsum + root.val

                self.ans = max(self.ans , current_sum)

                return (True , min(left_min , root.val) , max(right_max , root.val),current_sum)

            else :

                return (False , float('-inf') , float('inf'),0)

        solve(root)

        return self.ans        






        