# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """


        def bfs(root):
            if not root:
                return []
            q = deque([root])
            heap = []
            

            while q:
                level_sum = 0
                for _ in range(len(q)):

                    node = q.popleft()
                    level_sum += node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                # using min heap

                heapq.heappush(heap,level_sum)
                if len(heap) > k:
                    heapq.heappop(heap)

            if len(heap) < k:
                return -1

            return heap[0]     
        return bfs(root)           


        