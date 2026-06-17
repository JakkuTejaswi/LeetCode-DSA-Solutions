class Solution(object):
    def totalNumbers(self, digits):
        result=set()
        used=[False]*len(digits)
        def dfs(path):
            if len(path)==3:
                n=path[0]*100+path[1]*10+path[2]
                result.add(n)
                return
            for i in range(len(digits)):
                if used[i]:
                    continue
                if len(path)==0 and digits[i]==0:
                    continue
                if len(path)==2 and digits[i]%2!=0:
                    continue
                path.append(digits[i])
                used[i]=True
                dfs(path)
                path.pop()
                used[i]=False
        dfs([])
        return len(list(result))
        