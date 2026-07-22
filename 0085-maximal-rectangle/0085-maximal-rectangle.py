class Solution(object):


    def Rectangle(self , heights):
        
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
                
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        heights = [0]*cols
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                
                if matrix[i][j] == "1":
                    heights[j]+=1
                    
                    
                else:
                    heights[j] =0
                    
            ans = max(ans , self.Rectangle(heights))
            
        return ans   