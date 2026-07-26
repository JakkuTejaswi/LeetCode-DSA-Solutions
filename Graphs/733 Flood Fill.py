from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        n=len(image)
        m=len(image[0])
        visited=[[False]*m for _ in range(n)]
        c=image[sr][sc]
        q=deque()
        q.append((sr,sc))
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        image[sr][sc]=color
        visited[sr][sc]=True
        while q:
            x,y=q.popleft()
            for dx, dy in dir:
                nx=dx+x
                ny=dy+y
                if(0<=nx<n and 0<=ny<m and image[nx][ny]==c
                    and not visited[nx][ny]):
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    image[nx][ny]=color
        return image
