# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        stack=[(root, False)]
        diameter=0
        height={}
        while stack:
            node, visited=stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left=height.get(node.left, 0)
                right=height.get(node.right, 0)
                diameter=max(diameter, left+right)
                height[node]=max(left, right)+1
        return diameter

