import heapq
from typing import List, Tuple
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.kClosest_n(points, k)

    def kClosest_nlogk(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        n = len(points)

        def dist(p: List[int]) -> int:
            return p[0] * p[0] + p[1] * p[1]

        for i in range(n):
            if i < k:
                heapq.heappush(h, (-dist(points[i]), i))
            else:
                curr = dist(points[i])
                if curr < -h[0][0]:
                    heapq.heappushpop(h, (-curr, i))

        return [points[x[1]] for x in h]
    
    def kClosest_n(self, points: List[List[int]], k_orig: int) -> List[List[int]]:
        # compute all the distances (in float)
        # find the max distance
        # use the n/2th distance, and see how many points are below and above that.
        # 
        n = len(points)
        if k_orig == n:
            return points
        elif k_orig == 0:
            return []

        def compute_dist() -> Tuple[List[float], float]:
            dist = []
            max_dist = 0.0
            for i in range(n):
                d = math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1])
                dist.append(d)
                max_dist = max(d, max_dist)

            return (dist, max_dist)

        
        distances, max_dist = compute_dist()
        
        def input(index_arr: List[int], d: float) -> Tuple[List[int], List[int]]:
            lower = []
            higher = []
            m = len(index_arr)
            for i in range(m):
                if distances[index_arr[i]] <= d:
                    lower.append(index_arr[i])
                else:
                    higher.append(index_arr[i])
            
            return (lower, higher)

        # we need to figure out the distance that gives us k points.
        # first we take n/2 distance. and split into higher and lower points
        # three cases. 
        # lower = k (done)
        # lower < k (put all these into the list, and now look for k - lower in higher, i.e. input(higher, mid, k-lower))
        # lower > k (discard higher, input(lower, mid, k))
        # at the end, return the final list.

        
        result = []
        low = 0.0
        high = max_dist
       
        indexes = [i for i in range(n)]
        k = k_orig
        while k > 0:
            mid = (low + high) / 2.0
            lower, higher = input(indexes, mid)
            lower_len = len(lower)
            if lower_len <= k:
                result.extend(lower)
                k -= lower_len
                indexes = higher
                low = mid
            else:
                indexes = lower
                high = mid
        
        return [points[i] for i in result]
    
if __name__ == "__main__":
    s = Solution()
    points = [[1,3],[-2,2]]
    k = 1
    print(s.kClosest(points, k))