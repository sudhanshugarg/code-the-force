from typing import List, Tuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return self.carFleet2(target, position, speed)

    def carFleet1(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        car_colliding = [False] * n
        cars = zip(position, speed)
        print(len(car_colliding))

        for i in range(n):
            for j in range(i+1, n):
                #they could collide
                #find where they collide
                #if they collide after target, its fine, else
                point_of_collision, car = self.find_point(i, j, cars)
                if point_of_collision <= float(target):
                    #print(f"got car {car} going to collide with {i},{j}, at point {point_of_collision}")
                    car_colliding[car] = True
        
        ct = 0
        for i in range(n):
            if not car_colliding[i]:
                ct += 1
        
        return ct
    
    def find_point(self, i: int, j: int, cars: List[Tuple[int, int]]) -> Tuple[float, int]:
        #print(f"testing car {i} vs car {j}")
        #ensure car i starts earlier than car j
        if cars[i][0] > cars[j][0]:
            tmp = i
            i = j
            j = tmp

        position_i = cars[i][0]
        speed_i = cars[i][1]
        position_j = cars[j][0]
        speed_j = cars[j][1]
        if speed_i <= speed_j:
            return float("inf"), -1
        
        time_to_collision = float(position_j - position_i) / float(speed_i - speed_j)
        point_of_collision = float(position_i) + time_to_collision * float(speed_i)
        return point_of_collision, i

    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        n = len(cars)
        target_fp32 = float(target)

        slowest_car = 0
        fleets = 1
        for i in range(1, n):
            point_of_collision, _ = self.find_point(i, slowest_car, cars)
            #print(f"testing car {cars[i]}, slowest car = {cars[slowest_car]}, point_of_collision = {point_of_collision}")

            if point_of_collision > target_fp32:
                # slowest car is i
                slowest_car = i
                fleets += 1

        return fleets