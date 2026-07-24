# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def Preorder(root,level):
            if not root:
                return
            if len(result) == level:
                result.append(root.val)

            Preorder(root.right , level+1)
            Preorder(root.left , level + 1)
        Preorder(root , 0)
        return result            