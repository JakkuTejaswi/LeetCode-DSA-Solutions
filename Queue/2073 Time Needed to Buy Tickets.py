from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        q=deque()
        for i in range(len(tickets)):
            q.append((i, tickets[i]))
        time=0
        while q:
            idx, t=q.popleft()
            time+=1
            t-=1
            if t==0:
                if idx==k:
                    return time
            else:
                q.append((idx, t))
