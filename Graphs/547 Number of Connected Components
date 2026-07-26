from collections import deque
class Solution:
    def countConnected(self, V, edges):
        adj_mat=[[0]*V for _ in range(V)]
        for u,v in edges:
            adj_mat[u][v]=1
            adj_mat[v][u]=1
        visited=set()
        queue=deque()
        count=0
        for start in range(V):
            if start not in visited:
                count+=1
                visited.add(start)
                queue.append(start)
                while queue:
                    node=queue.popleft()
                    for i in range(V):
                        if adj_mat[node][i]==1 and i not in visited:
                            visited.add(i)
                            queue.append(i)
        return count
                
                    
            