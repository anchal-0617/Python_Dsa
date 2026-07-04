# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        ans = []

        def solve(root):
            

            if not root:
                return 0

            solve(root.left)
            ans.append(root.val)
            solve(root.right)
        solve(root)  
        

        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1]:
                return False

            
        return True