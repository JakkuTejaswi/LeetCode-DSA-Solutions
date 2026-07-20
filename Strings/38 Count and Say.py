class Solution(object):
    def countAndSay(self, n):
        temp="1"
        for j in range(n-1):
            count=1
            ans=""
            for i in range(1,len(temp)):
                if temp[i]==temp[i-1]:
                    count+=1
                else:
                    ans+=str(count)+temp[i-1]
                    count=1
            ans+=str(count)+temp[-1]
            temp=ans
        return temp

        
        