# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
        path = []
        result  = []
        def solve(root):
            if not root:
                return 

            path.append(root.val)

            if not root.left and not root.right:
            
                result.append("->".join(map(str, path)))        
    

            else:
                solve(root.left)
                solve(root.right)    
            path.pop()    
                   



        solve(root)

        return result  




            