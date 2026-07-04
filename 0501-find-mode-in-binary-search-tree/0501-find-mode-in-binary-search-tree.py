# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        
        
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """


        freq = {}

        def dfs(root):
            if not root:
                return

            freq[root.val] = freq.get(root.val, 0) + 1

            dfs(root.left)
            dfs(root.right)


        dfs(root)

        maxFreq = max(freq.values())

        ans = []

        for value, count in freq.items():
            if count == maxFreq:
                ans.append(value)

        return ans    
        # def solve(root):
            

        #     if not root:
        #         return 0

        #     solve(root.left)
        #     ans.append(root.val)
        #     solve(root.right)
        # solve(root)    

        # result = []
        # count = 1
        # max_count = float("-inf")
        # for i in range(1,len(ans)):
            
                
        #     if ans[i] == ans[i-1]:
        #         count = count+1
        #     max_count = max(max_count , count)

        #     return max_count
        # return solve(root)    


