# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return False
        stack=[root]
        row=[]
        while stack:
            node=stack.pop()
            row.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        row.sort()
        l=0
        r=len(row)-1
        while(l<r):
            if row[l]+row[r]==k:
                return True
            elif row[l]+row[r]>k:
                r-=1
            elif row[l]+row[r]<k:
                l+=1
        return False
        