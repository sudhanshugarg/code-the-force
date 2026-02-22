from typing import List
from enum import Enum

class Solution:
    def insert(self, intervals: List[List[int]], m: List[int]) -> List[List[int]]:
         return self.insert_linear(intervals, m)
    
    def insert_binsearch(self, intervals: List[List[int]], m: List[int]) -> List[List[int]]:

        # find the left most intersecting interval
        # find the right most intersecting interval
        # merge from i[0:l-1] + m + i[r+1:]

        n = len(intervals)
        def bin_search(index: int):
                t = m[index]
                low = 0
                high = n-1
                while low < high:
                     mid = (low + high) // 2
                     if t < intervals[mid][0]:
                          high = mid-1
                     elif t > intervals[mid][0]:
                          low = mid+1
                     else:
                          low = mid
                          break
                return low if intervals[low][0] <= t else low-1

        l = bin_search(0)
        # we always return an index such that the start of that interval < m[0]
        # need to check whether l intersects with newInterval or not
        # the start of l is <= start of newInterval
        # l then m
        # l and m overlap
        if l < 0:
             if m[1] > intervals[0][0]:
                  m[0] = min(m[0], intervals[0][0])
                  l = 0
        else: #there is an interval to the left
            if intervals[l][1] < m[0]: # l then m
                l += 1
            else: #they overlap
                m[0] = min(intervals[l][0], m[0])             

        r = bin_search(1)
        # r then m
        # r and m overlap
        if r < 0:
             r = 0
        else:
            if intervals[r][1] < m[1]: # r then m
                r += 1
            else:
                m[1] = max(intervals[r][1], m[1])


        ints2 = intervals[0:l]
        ints2.append(m)
        ints2.__add__(intervals[r+1:])
        return ints2
    
    def insert_linear(self, intervals: List[List[int]], m: List[int]) -> List[List[int]]:
         n = len(intervals)
         result = []

         def get_position(a: int) -> POS:
              other = intervals[a]

              if m[1] < other[0]:
                   return POS.LEFT
              elif m[0] > other[1]:
                   return POS.RIGHT
              return POS.OVERLAP
              
         for i in range(n):
              pos = get_position(i)
              #print(f"for interval {intervals[i]}, and {m}, got {pos}")
              if pos == POS.LEFT: #m is to the left
                   result.append(m)
                   for j in range(i, n):
                    result.append(intervals[j])
                   return result
              elif pos == POS.RIGHT:
                   result.append(intervals[i])
                   continue
              else:
                   m[0] = min(m[0], intervals[i][0])
                   m[1] = max(m[1], intervals[i][1])

         result.append(m)
         return result


class POS(Enum):
     LEFT = 1
     OVERLAP = 2
     RIGHT = 3