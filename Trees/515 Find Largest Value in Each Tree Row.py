# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        q=deque([root])
        res=[root.val]
        while q:
            row=[]
            for i in range(len(q)):
                node=q.popleft()
                if node.left is not None:
                    q.append(node.left)
                    row.append(node.left.val)
                if node.right is not None:
                    q.append(node.right)
                    row.append(node.right.val)
            if len(row)>0:
                maxi=max(row)
                res.append(maxi)
        return res