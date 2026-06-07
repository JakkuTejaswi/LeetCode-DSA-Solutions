class Solution(object):
    def getRow(self, rowIndex):
        res=[]
        for i in range(rowIndex+1):
            r=[1]*(i+1)
            for j in range(1,i):
                r[j]=res[i-1][j-1]+res[i-1][j]
            res.append(r)
        return res[-1]
