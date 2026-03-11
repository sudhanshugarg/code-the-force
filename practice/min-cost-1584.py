from collections import defaultdict
from collections.abc import Iterator
import heapq
from typing import List, Set

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.minCostConnectPointsPrims(points)
    
    def minCostConnectPointsKruskals(self, points: List[List[int]]) -> int:
        # compute the distances between all pairs of points
        # add tuple [dist, u, v] to a min-heap
        # create adj list for the graph that we are creating
        # in a loop:
        #   take out edge from heap
        # check if there is a path already between u, v
        # if yes, discard edge. else add it to the adj list
        # add both vertices to visited set.
        # stop when visited set size is n.
        n = len(points)
        heap = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, [dist, i, j])
        
        adj = defaultdict(list)
        counted = set()
        min_cost = 0
        num_edges = 0

        def path(u: int, v: int, visited: Set[int]) -> Iterator[bool]:
            if u == v:
                yield True
            
            if u in visited:
                yield False

            visited.add(u)
            nodes = adj[u]
            for i in nodes:
                if path(i, v, visited):
                    yield True
            
            yield False


        while num_edges < (n-1):
            e = heapq.heappop(heap)
            # print(f"testing edge {e}")
            if path(e[1], e[2], set()):
                # print(f"path already exists for edge {e}")
                continue

            # print(f"adding edge {e}")
            min_cost += e[0]
            num_edges += 1
            counted.add(e[1])
            counted.add(e[2])
            adj[e[1]].append(e[2])
            adj[e[2]].append(e[1])

        return min_cost
    
    
    def generator_playground(self, points: List[List[int]]) -> int:
        n = len(points)

        def path() -> Iterator[int]:
            for i in range(n):
                yield i
        
        res = list(path())
        print(res)
        return -1
    
    def minCostConnectPointsPrims(self, points: List[List[int]]) -> int:
        # take any point
        # add the closest point to it
        # then, add the next closest point to this set
        # keep adding closest points until all points are in the set
        # when you add a point, make sure its from the not chosen points
        # this way, there will never be a cycle.
        # to compute closest points, put the distances into a heap.

        n = len(points)
        heap = [[0, n-1]]
        visited = set()
        min_cost = 0

        while len(visited) < n:
            u = heapq.heappop(heap)
            if u[1] in visited:
                continue

            visited.add(u[1])
            min_cost += u[0]
            for v in range(n):
                if v in visited:
                    continue
                dist = abs(points[u[1]][0] - points[v][0]) + abs(points[u[1]][1] - points[v][1])
                heapq.heappush(heap, [dist, v])
        
        return min_cost


if __name__ == "__main__":
    s = Solution()
    p = [[2,-3],[-17,-8],[13,8],[-17,-15]]
    p = [[8, 1], [9, 2]]
    print(s.minCostConnectPoints(p))

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))