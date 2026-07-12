# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
    
        ans = []

        def solve(root,row,col):

            if root is None:

                return 

            ans.append((col , row , root.val))

            solve(root.left , row+1 , col-1)

            solve(root.right , row+1 , col+1)

        solve(root,0,0)

        ans.sort()


        result = []

        prev_col = float('-inf')

        for col , row , val in ans:

            if prev_col != col:
                result.append([])

                prev_col = col

            result[-1].append(val)

        return result        


