class Solution(object):
    def removeStars(self, s):
        stack=[]
        res=""
        for i in range(len(s)):
            if s[i]=="*":
                stack.pop()
            else:
                stack.append(s[i])
        res="".join(stack)
        return res
        