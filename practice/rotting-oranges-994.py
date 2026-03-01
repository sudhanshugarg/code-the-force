from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        minute = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while q:
            r, c, t = q.popleft()
            minute = t if t > minute else minute
            for i in range(4):
                nr = r + dir[i][0]
                nc = c + dir[i][1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1:
                    continue
                
                grid[nr][nc] = 2
                q.append((nr, nc, t+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return minute