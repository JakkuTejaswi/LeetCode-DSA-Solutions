# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        stack=[(root, root.val)]
        while stack:
            node, current_sum=stack.pop()
            if node.left is None and node.right is None:
                if current_sum==targetSum:
                    return True
            if node.right:
                stack.append((node.right, current_sum+node.right.val))
            if node.left:
                stack.append((node.left, current_sum+node.left.val))
        return False
