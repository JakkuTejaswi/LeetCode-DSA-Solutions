class Solution(object):
    def distributeCandies(self, candyType):
        s=set()
        n=len(candyType)//2
        count=0
        for i in range(len(candyType)):
            if candyType[i] not in s and len(s)<n:
                s.add(candyType[i])
        return len(s)
            
