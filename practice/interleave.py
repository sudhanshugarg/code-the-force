from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave2(s1, s2, s3)

    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
    
        m = len(s1)
        n = len(s2)

        if len(s3) != m+n:
            return False

        #3d array [i][j][2]
        dp = [[[False for _ in range(2)] for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n][0] = dp[m][n][1] = True # with two empty strings, we can create an empty string

        j = m + n - 1
        for i in range(m-1, -1, -1):
            dp[i][n][0] = dp[i+1][n][0] and (s3[j] == s1[i])
            dp[i][n][1] = False
            j -= 1
        
        i = m + n - 1
        for j in range(n-1, -1, -1):
            dp[m][j][1] = dp[m][j+1][1] and (s3[i] == s2[j])
            dp[m][j][0] = False
            i -= 1

        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                #pos in s3
                pos = j + i
                dp[i][j][0] = (s1[i] == s3[pos]) and (dp[i+1][j][0] or dp[i+1][j][1])
                dp[i][j][1] = (s2[j] == s3[pos]) and (dp[i][j+1][0] or dp[i][j+1][1])
        
        return dp[0][0][0] or dp[0][0][1]

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
    
        m = len(s1)
        n = len(s2)

        if len(s3) != m+n:
            return False

        #3d array [i][j][2]
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n] = True # with two empty strings, we can create an empty string

        j = m + n - 1
        for i in range(m-1, -1, -1):
            dp[i][n] = dp[i+1][n] and (s3[j] == s1[i])
            j -= 1
        
        i = m + n - 1
        for j in range(n-1, -1, -1):
            dp[m][j] = dp[m][j+1] and (s3[i] == s2[j])
            i -= 1

        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                #pos in s3
                pos = j + i
                dp[i][j] = ((s1[i] == s3[pos]) and dp[i+1][j]) or ((s2[j] == s3[pos]) and dp[i][j+1])
        
        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("ab", "cde", "cdaeb"))
