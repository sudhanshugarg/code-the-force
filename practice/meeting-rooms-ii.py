class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        #sort all the 2n points
        #then go one by one
        n = len(intervals)
        points = list()
    
        for i in range(n):
            s = Point(intervals[i][0], 1)
            e = Point(intervals[i][1], 0)
            points.append(s)
            points.append(e)
        
        points.sort()
        rooms = 0
        max_rooms = 0
        for i in range(2*n):
            if points[i].is_start:
                rooms += 1
            else:
                rooms -= 1
        
            max_rooms = rooms if rooms > max_rooms else max_rooms
        return max_rooms

class Point:
    def __init__(self, a: int, is_start: int):
        self.a = a
        self.is_start = is_start
    
    def __lt__(self, other) -> bool:
        if self.a < other.a:
            return True
        elif self.a == other.a:
            return self.is_start < other.is_start
        else:
            return False