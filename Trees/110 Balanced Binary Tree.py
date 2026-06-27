# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        stack=[(root, False)]
        height={}
        while stack:
            node, visited=stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left=height.get(node.left,0)
                right=height.get(node.right, 0)
                if abs(left-right)>1:
                    return False
                height[node]=1+max(left, right)
        return True
        