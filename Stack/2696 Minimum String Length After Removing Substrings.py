class Solution(object):
    def minLength(self, s):
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if (len(stack)>0) and (s[i]=='B' and stack[-1]=='A' or s[i]=='D' and stack[-1]=='C'):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
        