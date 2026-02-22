from typing import List
from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search on time
        # find max time
        # then for each time, find whether or not there is a path
        # O(mn log T) - where T is the max time.
        maxTime = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                maxTime = maxTime if maxTime > grid[i][j] else grid[i][j]

        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def is_path(t: int) -> bool:
            q = deque()
            q.append([0, 0])
            dst = [m-1, n-1]
            visited = [[False for _ in range(n)] for _ in range(m)]


            while len(q) > 0:
                curr = q.popleft()
                if curr[0] == dst[0] and curr[1] == dst[1]:
                    return True

                if visited[curr[0]][curr[1]]:
                    continue

                visited[curr[0]][curr[1]] = True
                for i in range(4):
                    nr = curr[0] + dir[i][0]
                    nc = curr[1] + dir[i][1]
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc] or grid[nr][nc] > t:
                        continue
                    q.append([nr, nc])
            return False


        low = grid[0][0]
        high = maxTime
        while low < high:
            mid = int((low + high) / 2)
            canGo = is_path(mid)
            # print(f"testing {low}, {high} => {mid}, {canGo}")
            if canGo:
                high = mid-1
            else:
                low = mid+1
        
        return low if is_path(low) else low+1

if __name__ == "__main__":
    s = Solution()
    # g = [[0,2],[1,3]]
    # g = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    # g = [[5,5],[2,1]]
    # g = [[5,4],[6,0]]
    g = [[2,3],[1,0]]
    print(s.swimInWater(g))
    


