class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindromeExpand(s)

    def longestPalindromeDp(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        index = [0, 0]
        for i in range(n):
            dp[i][i] = True
            if i < (n-1):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    index[0] = i
                    index[1] = i+1

        for k in range(3, n):
            for i in range(n-k+1):
                j = i + k - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    index[0] = i
                    index[1] = j
        
        return s[index[0]:index[1]+1]
    
    def longestPalindromeExpand(self, s: str) -> str:
        n = len(s)
        # start from each position. move outwards
        # either start with each index as the middle element
        # or start with each index and the right one, as the middle 2.
        # if you already have a largest so far, start from there itself, don't need to check the smaller
        # ones. actually we still do need to check the smaller ones.


        def expand(l:int, r:int) -> List[int]:
            # print(f"checking [{l},{r}]")
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            if r == l+1:
                # print(f"returning [{l},{l+1}]")
                return [l, l+1]
            else:
                # print(f"returning [{l+1},{r-1}]")
                return [l+1, r-1]

        def len_palin(a: List[int]) -> int:
            return a[1] - a[0] + 1
        
        max_palin = [0, 0]
        for i in range(n):
            # odd
            palin = expand(i, i)
            max_palin = palin if len_palin(palin) > len_palin(max_palin) else max_palin
            # even
            if i < n-1 and s[i] == s[i+1]:
                palin = expand(i, i+1)
                max_palin = palin if len_palin(palin) > len_palin(max_palin) else max_palin
        
        l = max_palin[0]
        r = max_palin[1]
        return s[l:r+1]
