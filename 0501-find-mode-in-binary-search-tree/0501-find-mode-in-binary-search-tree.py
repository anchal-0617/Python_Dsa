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


        # freq = {}

        # def dfs(root):
        #     if not root:
        #         return

        #     freq[root.val] = freq.get(root.val, 0) + 1

        #     dfs(root.left)
        #     dfs(root.right)


        # dfs(root)

        # maxFreq = max(freq.values())

        # ans = []

        # for value, count in freq.items():
        #     if count == maxFreq:
        #         ans.append(value)

        # return ans  
        
        ans = []

        def solve(root):
            if not root:
                return

            solve(root.left)
            ans.append(root.val)
            solve(root.right)

        solve(root)

        if not ans:
            return []

        count = 1
        max_count = 1

        # First pass: Find maximum frequency
        for i in range(1, len(ans)):
            if ans[i] == ans[i - 1]:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)

        # Second pass: Collect all modes
        result = []
        count = 1

        if len(ans) == 1:
            return ans

        for i in range(1, len(ans)):
            if ans[i] == ans[i - 1]:
                count += 1
            else:
                count = 1

            if count == max_count:
                result.append(ans[i])

        # Handle the case where every element appears once
        if max_count == 1:
            return list(set(ans))

        return result    


