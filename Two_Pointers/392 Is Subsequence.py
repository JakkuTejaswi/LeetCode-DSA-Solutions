class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)<1:
            return True
        r=0
        found=[False]*len(s)
        for i in range(len(s)):
            for j in range(r,len(t)):
                if s[i]==t[j]:
                    found[i]=True
                    r+=1
                    break
                r+=1
        if False in found:
            return False
        return True
        