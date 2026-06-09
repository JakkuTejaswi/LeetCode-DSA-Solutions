class Solution(object):
    def backspaceCompare(self, s, t):
        s1=[]
        s2=[]
        for ch in s:
            if ch!="#":
                s1.append(ch)
            elif s1:
                s1.pop()
        for ch in t:
            if ch!="#":
                s2.append(ch)
            elif s2:
                s2.pop()
        return "".join(s1)=="".join(s2)        

        