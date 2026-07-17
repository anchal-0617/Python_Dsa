class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """


        n = len(isConnected)
        visited = [False] * n

        provinces = 0

        def solve(node):
            visited[node] = True

            for neighbours in range(n):
                if isConnected[node][neighbours] == 1 and not visited [neighbours]:

                    solve(neighbours)

        for i in range(n):
            if not visited[i] :
                provinces += 1
                solve(i)

        return provinces                    
        