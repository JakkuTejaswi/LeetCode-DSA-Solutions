# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        stack=[root]
        d={}
        maxi=0
        while stack:
            node=stack.pop()
            d[node.val]=d.get(node.val,0)+1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        for key in d:
            if d[key]>=maxi:
                maxi=d[key]
        res=[key for key in d if d[key]==maxi]
        return res
        
