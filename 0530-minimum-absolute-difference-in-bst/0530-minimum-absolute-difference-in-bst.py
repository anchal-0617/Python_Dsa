# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = []

        def solve(root):
            

            if not root:
                return 0

            solve(root.left)
            ans.append(root.val)
            solve(root.right)
        solve(root)  
        value = 0
        min_value = float("inf")

        for i in range(1,len(ans)):
            value = ans[i] - ans[i-1]

            min_value = min(min_value , value)

        return min_value    