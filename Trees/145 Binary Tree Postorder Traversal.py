# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        st1=[]
        st2=[]
        res=[]
        if root is None:
            return []
        st1.append(root)
        while st1:
            curr=st1.pop()
            st2.append(curr)
            if curr.left:
                st1.append(curr.left)
            if curr.right:
                st1.append(curr.right)
        while st2:
            res.append(st2.pop().val)
        return res
            

        