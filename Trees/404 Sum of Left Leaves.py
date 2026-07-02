# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        stack=[(root,False)]
        sum=0
        while stack:
            node,visited=stack.pop()
            if node.left is not None:
                stack.append((node.left, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is None and node.right is None and visited is True:
                sum+=node.val
        return sum