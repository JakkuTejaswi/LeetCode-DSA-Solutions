class Solution(object):
    def plusOne(self, digits):
        n=0
        for num in digits:
            n=n*10+num
        n=n+1
        rem=0
        r=[]
        while n>0:
            rem=n%10
            r.append(rem)
            n=n//10
        return r[::-1]


