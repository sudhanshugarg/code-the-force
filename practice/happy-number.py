class Solution:
    def isHappy(self, n: int) -> bool:
        def compute_next(n: int) -> int:
            ans = 0
            while n > 0:
                r = n % 10
                ans += r * r
                n = int(n / 10)
            return ans

        visited = set()
        curr = n
        while curr != 1 and curr not in visited:
            visited.add(curr)
            curr = compute_next(curr)
        
        return curr % 10 == 1

