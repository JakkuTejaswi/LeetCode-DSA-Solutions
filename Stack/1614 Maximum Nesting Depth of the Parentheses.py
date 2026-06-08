class Solution(object):
    def maxDepth(self, s):
        stack=[]
        count=0
        max_count=0
        for ch in s:
            if ch=="(":
                stack.append(ch)
            elif ch==")":
                if stack:
                    count=len(stack)
                    max_count=max(max_count,count)
                    count=0
                    stack.pop()
        return max_count
