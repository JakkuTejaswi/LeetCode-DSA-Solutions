# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        stack=[]
        res=[]
        current=root
        while stack or current:
            while current:
                stack.append(current)
                current=current.left
            current=stack.pop()
            res.append(current.val)
            current=current.right
        return res

