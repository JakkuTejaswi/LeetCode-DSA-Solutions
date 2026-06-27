# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        stack=[root]
        while stack:
            node=stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            node1=node.left
            node.left=node.right
            node.right=node1
        return root

        

        