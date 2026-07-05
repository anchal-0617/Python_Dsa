# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def solve(root):
            if not root:
                return 0
            q = deque([(root,0)])

            ans = 0
           

            while q:
                size = len(q)

                first = q[0][1]
                left = right = 0

                for i in range(size):

                    node , idx = q.popleft()


                    idx = idx - first

                    if i == 0:
                        left = idx

                    if i == size - 1:
                        right = idx

                    if node.left:
                        q.append((node.left,2*idx + 1))

                    if node.right:
                        q.append((node.right , 2 * idx +2))



                ans = max(right - left + 1 , ans) 
            return ans  

        return solve(root)     




