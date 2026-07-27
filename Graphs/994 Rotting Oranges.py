from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        queue = deque()
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited[i][j] = True
        dir = [(-1,0), (1,0), (0,1), (0,-1)]
        while queue:
            size = len(queue)
            count = 0
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in dir:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < n and
                        0 <= ny < m and
                        not visited[nx][ny] and
                        grid[nx][ny] == 1):
                        queue.append([nx, ny])
                        visited[nx][ny] = True
                        grid[nx][ny] = 2
                        count += 1
            if count > 0:
                c += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return c