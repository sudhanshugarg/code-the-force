from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.findRedundantConnectionCycle(edges)

    def findRedundantConnectionBrute(self, edges: List[List[int]]) -> List[int]:
        return []
    
    def findRedundantConnectionCycle(self, edges: List[List[int]]) -> List[int]:
        # find the cycle
        # once we have the edges in teh cycle, return the edge with the largest index
        # lets find n, number of vertices
        # it is len(edges)

        n = len(edges) # for this problem
        adj = defaultdict(list)
        for i in range(n):
            e = edges[i]
            adj[e[0]].append([e[1], i])
            adj[e[1]].append([e[0], i])

        visited = [False for _ in range(n+1)]
        edges_curr = list()

        def dfs(u: int, parent: int):
            # found cycle
            if visited[u]:
                return True, u
            
            visited[u] = True
            vs = adj[u]
            for v in vs:
                if v[0] == parent:
                    continue

                edges_curr.append(v[1])
                found_cycle, cycle_start = dfs(v[0], u)
                if found_cycle:
                    return True, cycle_start
                edges_curr.pop()
            
            visited[u] = False
            return False, 0

        _, cycle_start = dfs(n, 0)
        print(f"{cycle_start} => {edges_curr}")
        m = len(edges_curr)
        highest_index = edges_curr[m-1]
        for i in range(m-2, -1, -1):
            e = edges_curr[i]
            highest_index = e if e > highest_index else highest_index
            if edges[e][0] == cycle_start or edges[e][1] == cycle_start:
                break

        return edges[highest_index]

if __name__ == "__main__":
    s = Solution()
    e = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    res = s.findRedundantConnectionCycle(e)
    print(res)