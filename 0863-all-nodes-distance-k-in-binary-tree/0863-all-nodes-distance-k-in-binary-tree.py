# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent = {}
        def solve(root):
            if not root:
                return 

            if root.left:
                parent[root.left] = root
            solve(root.left)

            if root.right:
                parent[root.right] = root
            solve(root.right)   

        solve(root)      


        q = deque([target])
        visited = set()
        visited.add(target)

        while q:
            if k == 0:
                break

            for _ in range(len(q)):
                node = q.popleft()

                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    q.append(node.right)    
                    visited.add(node.right)

                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited.add(parent[node]) 

            k-=1

        ans = []

        while q:
            ans.append(q.popleft().val)

        return ans                



