# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=deque([root])
        res=[[root.val]]
        count=0
        while q:
            row=[]
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    row.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    row.append(node.right.val)
            count+=1
            if len(row)>0:
                if count%2==0:
                    res.append(row)
                else:
                    row.reverse()
                    res.append(row)
        return res
            

        
        