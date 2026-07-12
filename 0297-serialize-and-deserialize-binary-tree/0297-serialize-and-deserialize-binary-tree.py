# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def solve(root):
            
            if root is None:
                ans.append("null")

                return

            ans.append(str(root.val))

            solve(root.left)
            solve(root.right)
        solve(root)

        return ",".join(ans)            

            

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.i = 0    

        def solve():
            if values[self.i] == "null":
                self.i +=1
                return None

            root = TreeNode(int(values[self.i]))
            self.i +=1

            root.left = solve()

            root.right = solve()

            return root

        return solve()        



        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))