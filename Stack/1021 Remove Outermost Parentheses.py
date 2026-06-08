class Solution(object):
    def removeOuterParentheses(self, s):
        stack=[]
        ans=[]
        for ch in s:
            if ch=="(":
                if stack:
                    ans.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if stack:
                    ans.append(ch)
        return "".join(ans)
        
