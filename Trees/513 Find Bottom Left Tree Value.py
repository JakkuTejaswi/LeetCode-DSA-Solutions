# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        q=deque([root])
        row=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.right is not None:
                    q.append(node.right)
                    row.append(node.right.val)
                if node.left is not None:
                    q.append(node.left)
                    row.append(node.left.val)
        return row[-1]

            