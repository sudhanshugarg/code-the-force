class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.myPow_binary(x, n)

    def myPow_linear(self, x: float, n: int) -> float:
        #n operations
        if n == 0:
            return 1.0
        
        ans = x
        for i in range(n-1):
            ans *= x
        
        return ans

    def myPow_binary(self, x: float, n: int) -> float:
        #log n times.
        # find the binary representation of n
        # for each time it is 1, we multiply the appropriate value
        # there are a few cases.
        multiplier = 1.0
        if x < 0 and (n % 2 != 0):
            multiplier = -1.0        

        orig_x = x
        if x < 0:
            x = -x
            orig_x = -orig_x
        
        reciprocal = False
        one_more = False
        if n == -2147483648:
            n = -2147483647
            one_more = True

        if n < 0:
            reciprocal = True
            n = -n

        ans = 1.0

        while n > 0:
            use = n % 2
            if use > 0:
                ans *= x
            x = x * x
            n = int(n / 2)

        if not reciprocal:
            return multiplier * ans
        else:
            if one_more:
                return multiplier / (ans * orig_x)
            else:
                return multiplier / ans