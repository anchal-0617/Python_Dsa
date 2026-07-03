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
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def solve(root,summ):
            if not root:
                return 0
            
            path.append(root.val)
            summ += root.val

            if not root.left and not root.right:
                if summ == targetSum:
                    result.append(path[:])

            else:
                solve(root.left,summ)
                solve(root.right,summ)

            path.pop()    

        solve(root,0)    

        return result


