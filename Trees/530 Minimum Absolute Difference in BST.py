# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        res.sort()
        mini=abs(res[0]-res[1])
        l=1
        for r in range(2,len(res)):
            if abs(res[l]-res[r])<mini:
                mini=abs(res[l]-res[r])
            l+=1
        return mini