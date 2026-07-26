from collections import deque
class Solution(object):
    def numIslands(self, grid):
        count=0
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for _ in range(n)]
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            visited[i][j]=True
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                x,y=q.popleft()
                for dx, dy in directions:
                    nx=dx+x
                    ny=dy+y
                    if (0<=nx<n and 0<=ny<m and 
                        not visited[nx][ny] and grid[nx][ny]=='1'):
                        q.append((nx,ny))
                        visited[nx][ny]=True
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not visited[i][j]:
                    bfs(i,j)
                    count+=1
        return count

