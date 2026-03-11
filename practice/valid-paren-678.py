class Solution:
    def checkValidString(self, s: str) -> bool:
        # have a helper named recurse
        # pass to it, number of open brackets so far
        # each time we see a *, we start three recurses
        # if any of them is true, return true, else false.
        # also some optimizations, like if count of open brackets is greater than length of remaining
        # string, return false.

        # speed ups
        # count open, and close brackets.
        # open - close
        # these are the max number of *s to convert
        # when doing recurse, also pass how many converts left. if no converts left, return False.

        n = len(s)
        l = 0
        r = 0
        asterisk = 0
        for i in range(n):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            else:
                asterisk += 1

        if asterisk < abs(l-r):
            return False

        def recurse(open_braces: int, index: int, left_asterisks_to_use: int, right_asterisks_to_use: int) -> bool:
            if index == n:
                return open_braces == 0

            # not enough letters for closing brackets
            if (n - index) < open_braces:
                return False
            
            if left_asterisks_to_use < 0 or right_asterisks_to_use < 0:
                return False
            
            for i in range(index, n):
                if s[i] == '(':
                    open_braces += 1
                elif s[i] == ')':
                    if open_braces == 0:
                        return False
                    open_braces -= 1
                else: # *
                    if left_asterisks_to_use > 0:
                        return recurse(open_braces, i+1, left_asterisks_to_use - 1, 0) or \
                            (open_braces > 0 and recurse(open_braces-1, i+1)) or \
                                recurse(open_braces+1, i+1)

            return open_braces == 0        
        
        if l <= r:
            return recurse(0, 0, r-l, 0)
        else:
            return recurse(0, 0, 0, l-r)
    

if __name__ == "__main__":
    s = Solution()
    p = "(**********************************("
    print(s.checkValidString(p))