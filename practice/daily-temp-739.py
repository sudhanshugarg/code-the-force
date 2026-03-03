class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days = [n] * n
        for i in range(n-2, -1, -1):
            next_warmer = i+1
            while next_warmer != n and temperatures[i] >= temperatures[next_warmer]:
                next_warmer = days[next_warmer]
            days[i] = next_warmer

        for i in range(n):
            if days[i] == n:
                days[i] = 0
            else:
                days[i] -= i
        
        return days