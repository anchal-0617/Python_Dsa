# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """


        def match(head,root):
            if head == None:
                return True
            if root == None:
                return False

            if head.val != root.val:
                return False

            left = match(head.next, root.left)

            right = match(head.next , root.right)   

            return left or right 

        def solve(root):
            if not root:
                return False

            left1 = solve(root.left)

            right1 = solve(root.right)

            return ( match(head , root ) or left1 or right1)

        return solve(root)    

