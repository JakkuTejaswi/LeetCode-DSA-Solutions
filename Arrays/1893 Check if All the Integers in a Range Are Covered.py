class Solution(object):
    def isCovered(self, ranges, left, right):
        r=[]
        for i in range(left, right+1):
            r.append(i)
        found=[False]*len(r)
        for i in range(len(r)):
            for j in range(len(ranges)):
                if ranges[j][0]<=r[i]<=ranges[j][1]:
                    found[i]=True
                    break
        if False in found:
            return False
        return True
