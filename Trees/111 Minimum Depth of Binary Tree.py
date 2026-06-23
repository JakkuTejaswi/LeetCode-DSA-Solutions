# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        q=deque([root])
        count=1
        res=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    res.append(count)
            count+=1
        return min(res)
        