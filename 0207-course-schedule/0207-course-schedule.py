class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for u , v in prerequisites:
            adj[v].append(u)

            indegree[u] += 1

        q = deque()
            
        for i in range (numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
                
            for neighbour in adj[node]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)


        return count == numCourses            

                      


