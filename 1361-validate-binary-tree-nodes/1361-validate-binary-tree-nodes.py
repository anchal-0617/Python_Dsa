class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """


        def solve(leftChild,rightChild):
            parent = [-1] * n

            for i in range(n):
                if leftChild[i] != -1:
                    if parent[leftChild[i]] != -1:
                        return False
                    parent[leftChild[i]] = i

                if rightChild[i] != -1:

                    if parent[rightChild[i]] != -1:
                        return False
                    parent[rightChild[i]] = i

            print(parent)        


            root = -1

            for i in range(n):
                if parent[i] == -1:

                    if root != -1:
                        return False

                    root = i 
            if root == -1:
                return False        

            # tarversal / connected

            visited = set()

            def solve(root):

                if root == -1 or root in visited:
                    return 
                    
                    
                visited.add(root)    

                solve(leftChild[root])

                solve(rightChild[root])

            solve(root)    


            return  len(visited) == n   

        return solve(leftChild,rightChild)




        