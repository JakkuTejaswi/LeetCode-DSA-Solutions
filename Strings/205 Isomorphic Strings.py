class Solution(object):
    def isIsomorphic(self, s, t):
        d1={}
        d2={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            w=s[i]
            p=t[i]
            if w in d1 and d1[w]!=p:
                return False
            if w not in d1:
                d1[w]=p
        for i in range(len(t)):
            w=t[i]
            p=s[i]
            if w in d2 and d2[w]!=p:
                return False
            if w not in d2:
                d2[w]=p
        return True
        