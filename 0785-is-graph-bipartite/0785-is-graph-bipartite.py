class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """


        n = len(graph)

        color = [-1] * n

        def solve(curr , currcolor):
            color[curr] = currcolor
            for neighbour in graph[curr]:
                if color[neighbour] ==  color[curr]:
                    return False

                if color[neighbour] == -1:
                    colorofneighbour = 1 - currcolor

                    if solve(neighbour ,colorofneighbour ) == False:
                        return False

            return True   

        for i in range(n):

            if color[i] == -1:
                if solve(i , 1) == False:
                    return False

        return True         

        