class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        n = len(heights)
        
        prev = [-1] *n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
                
            stack.append(i)
        stack = []
        nxt = [n]*n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
                
            stack.append(i)   
        ans = 0
        for i in range(n):
            width = nxt[i] - prev[i] - 1
            ans = max(ans , heights[i] * width)
        return ans   
        