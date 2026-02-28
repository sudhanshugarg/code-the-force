from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.numDistinct2(s, t)
    
    def numDistinct1(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        assert m > 0 and n > 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        # we'll iterate over t first.
        # dp[i][j] means how many distinct subsequences of length s[0:i] can make t[0:j].

        for j in range(1, n+1):
            for i in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        # self.print(dp, m, n)
        return dp[m][n]

    def numDistinct2(self, s: str, t: str) -> int:
        # space should be O(m)
        m = len(s)
        n = len(t)

        assert m > 0 and n > 0
        dp = [[0 for _ in range(2)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1

        # we'll iterate over t first.
        # dp[i][j] means how many distinct subsequences of length s[0:i] can make t[0:j].

        # self.print_row(dp, m, 0)
        for j in range(1, n+1):
            k = j % 2
            for i in range(1, m+1):
                dp[i][k] = dp[i-1][k]
                if s[i-1] == t[j-1]:
                    dp[i][k] += dp[i-1][1-k]
            
            for i in range(m):
                dp[i][1-k] = 0

            # self.print_row(dp, m, k)
        
        return dp[m][n%2]

    def print_row(self, dp: List[List[int]], m: int, k: int):
        arr = []
        for j in range(m+1):
            arr.append(dp[j][k])
        print(arr)

    def print(self, dp: List[List[int]], m: int, n: int):
        for i in range(n+1):
            arr = []
            for j in range(m+1):
                arr.append(dp[j][i])
            print(arr)
        print("\n")