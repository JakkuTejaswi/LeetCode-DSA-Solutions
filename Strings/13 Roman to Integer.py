class Solution(object):
    def romanToInt(self, s):
        d={}
        d['I']=1
        d['V']=5
        d['X']=10
        d['L']=50
        d['C']=100
        d['D']=500
        d['M']=1000
        sum=0
        for i in range(len(s)):
            curr=s[i]
            if i+1<len(s):
                next=s[i+1]
                if d[curr]<d[next]:
                    sum-=d[curr]
                else:
                    sum+=d[curr]
            else:
                sum+=d[curr]
        return sum
        