from typing import List, Dict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        return self.findCheapestPrice_bellman_ford(n, flights, src, dst, k)

    def findCheapestPrice_djikstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adj list
        # start from src
        # create a visited set of [i, k]. ensure we never add src back to this set.
        # add [src, 0] to the heap
        # keep taking out from heap with least distance
        # end when heap is empty or dst is reached.

        adj = [[-1 for _ in range(n)] for _ in range(n)]
        m = len(flights)
        for i in range(m):
            a = flights[i][0]
            b = flights[i][1]
            c = flights[i][2]
            adj[a][b] = c

        pq = []
        heapq.heappush(pq, Node(src, 0, -1))
        visited = set()

        while len(pq) > 0:
            curr_node = heapq.heappop(pq)
            # print(f"visiting {curr_node}")
            if curr_node.id == dst:
                return curr_node.dist
            
            # cannot make any more stops
            if curr_node.stops == k:
                continue

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for i in range(n):
                if adj[curr_node.id][i] < 0 or i == src:
                    continue

                # there is a path
                # add to the heap only if not already visited
                next_node = Node(i, curr_node.dist + adj[curr_node.id][i], curr_node.stops + 1)
                #print(f"considering {next_node}")
                if next_node not in visited:
                    # print(f"adding {next_node}")
                    heapq.heappush(pq, next_node)

        return -1

    def findCheapestPrice_floyd(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[float("inf") for _ in range(n)] for _ in range(n)]

        m = len(flights)
        for i in range(m):
            a = flights[i][0]
            b = flights[i][1]
            adj[a][b] = float(flights[i][2])

        # floyd warshall

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
        
        self.print(adj, n)
        return self.get_inf(adj[src][dst])

    def findCheapestPrice_bellman_ford(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # keep a single array of distances (in float)
        # initialize all to inf, and src to 0
        # go over k loops
        # in each loop, go over all edges (m) 
        #   update the distance for each edge
        # eventually, return arr[dst]

        m = len(flights)

        dist = [[float('inf') for _ in range(2)] for _ in range(n)]
        dist[src][0] = dist[src][1] = 0

        r = 0
        for _ in range(k+1):
            r = 1 - r
            for e in range(m):
                u = flights[e][0]
                v = flights[e][1]
                cost = float(flights[e][2])

                if dist[v][r] > (dist[u][1-r] + cost):
                    dist[v][r] = dist[u][1-r] + cost

        return self.get_inf(dist[dst][r])

    def print(self, adj: List[List[float]], n: int):
        for i in range(n):
            arr = [self.get_inf(adj[i][j]) for j in range(n)]
            print(arr)
        print()

    def get_inf(self, a: float) -> int:
        return -1 if a == float("inf") else int(a)

class Node:
    def __init__(self, id: int, dist: int, stops: int):
        self.id = id
        self.dist = dist
        self.stops = stops
    
    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other) -> bool:
        return self.id == other.id and self.stops == other.stops
    
    def __hash__(self) -> int:
        return hash(hash(self.id) + hash(self.stops) + hash(self.dist))
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"[{self.id}, {self.dist}, {self.stops}]"