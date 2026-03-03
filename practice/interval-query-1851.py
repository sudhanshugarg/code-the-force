from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # keep two sorted lists
        # one by start
        # one by end
        # for each query, find the index of start
        # similarly, find the index of end
        # then find the first common interval, going right to left in start, and left to right in end
        # return that, or if none, then return -1.
        # optimization: speed up the finding of the first common interval. preprocess and keep all saved.

        debug = False
        def dprint(x):
            if debug:
                print(x)

        m = len(intervals)
        starts = []
        ends = []
        for i in range(m):
            starts.append([intervals[i][0], i])
            ends.append([intervals[i][1], i])
        
        
        starts.sort()
        ends.sort()
        dprint(intervals)
        dprint(starts)
        dprint(ends)

        def bin_search(target: int, is_starts: bool) -> int:
            # should return the index of the rightmost point, i.e. <= t
            low = 0
            high = m-1
            if is_starts:
                arr = starts
            else:
                arr = ends

            while low < high:
                mid_index = (low + high) // 2
                mid = arr[mid_index][0]
                dprint(f"checking mid={mid}")
                if target < mid:
                    high = mid_index-1
                elif target > mid:
                    low = mid_index+1
                else:
                    dprint(f"in equals with {mid}")
                    if is_starts:
                        low = mid_index
                        while low < (m-1) and arr[low+1][0] == target:
                            low += 1
                        return low
                    else:
                        low = mid_index
                        while low > 0 and arr[low-1][0] == target:
                            low -= 1
                        return low
            
            return low if arr[low][0] <= target else low-1

        def contains(id: int, q: int) -> bool:
            return intervals[id][0] <= q and intervals[id][1] >= q

        def get_smaller(container, id):
            if container == -1:
                return id
            
            if (intervals[container][1] - intervals[container][0]) < (intervals[id][1] - intervals[id][0]):
                return container
            else:
                return id
        
        def size(id: int) -> int:
            return intervals[id][1] - intervals[id][0] + 1

        result = []
        n = len(queries)
        for i in range(n):
            l_index = bin_search(queries[i], True)
            r_index = bin_search(queries[i], False)
            dprint(f"for query: {queries[i]}, found l: {l_index}, r: {r_index}")
            if r_index < 0:
                r_index += 1

            container = -1
            for j in range(l_index, -1, -1):
                id = starts[j][1]
                if contains(id, queries[i]):
                    container = get_smaller(container, id)
            
            dprint(f"lowest container left is {container}")

            for j in range(r_index, m):
                id = ends[j][1]
                if contains(id, queries[i]):
                    container = get_smaller(container, id)
            dprint(f"lowest container right is {container}")

            dprint(f"query: {queries[i]}, container: {container}")
            if container == -1:
                result.append(-1)
            else:    
                result.append(size(container))
        
        return result

if __name__ == "__main__":
    s = Solution()
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    print(s.minInterval(intervals, queries))