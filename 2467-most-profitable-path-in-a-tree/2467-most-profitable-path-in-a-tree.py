class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        adj = defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        n = len(amount)    

        bobtime = [float("inf")] * n
        ans = [float("-inf")]  
        def dfs(node,parent,time):
            if node == 0:
                bobtime[node] = time
                return True
            for i in adj[node]:
                if i == parent:  #infinity loop
                    continue      

                if dfs(i,node,time+1):
                    bobtime[node] = time
                    return True
            return False
        def Alice(node,parent,time,profit):
            
            if time<bobtime[node]:
                profit += amount[node]

            elif time == bobtime[node]:
                profit += amount[node] // 2

            if len(adj[node]) == 1 and node!=0:
                ans[0] = max(ans[0],profit)
                return 


            for i in adj[node]:
                if i == parent:
                    continue
                Alice(i,node,time+1 , profit)

        dfs(bob,-1,0)
        Alice(0,-1,0,0)

        return ans[0]        

