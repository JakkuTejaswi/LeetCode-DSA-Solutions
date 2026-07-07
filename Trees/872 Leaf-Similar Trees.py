# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        if root1 is None or root2 is None:
            return False
        if (root1.left is None and root2.left is None) and (root2.left is None and root2.right is None):
            if root1.val==root2.val:
                return True
            return False
        stack1=[root1]
        stack2=[root2]
        r1=[]
        r2=[]
        while stack1:
            node=stack1.pop()
            if node.right is not None:
                stack1.append(node.right)
            if node.left is not None:
                stack1.append(node.left)
            if node.left is None and node.right is None:
                r1.append(node.val)
        while stack2:
            node=stack2.pop()
            if node.right is not None:
                stack2.append(node.right)
            if node.left is not None:
                stack2.append(node.left)
            if node.left is None and node.right is None:
                r2.append(node.val)
        return True if r1==r2 else False




        