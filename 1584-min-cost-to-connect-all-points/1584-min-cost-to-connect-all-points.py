class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        visited = [False] * n

        minheap = [(0,0)]

        finalcost = 0

        while minheap:
            cost , node = heapq.heappop(minheap)

            if visited[node]:
                continue

            visited[node] =True

            finalcost += cost
            x1 , y1 = points[node]

            for neighbour in range (n):

                if not visited[neighbour]:

                    x2 , y2 = points[neighbour]

                    distance = abs(x1-x2) + abs(y1-y2)

                    heapq.heappush(minheap , (distance , neighbour))

        return finalcost            

