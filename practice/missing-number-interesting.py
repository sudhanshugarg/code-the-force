from typing import Set

class Solution:
    def findMissingNumber(self, s: str, n: int) -> int:
        # lets say n = 12
        # the string is 12111098765432
        # the missing number is 1
        # we calculate the following: given a set of numbers so far
        # and the position i, what is the missing number
        # if it isn't possible, then we return 0
        # 
        # now, we start at position i
        # we also should pass the number of digits d in n
        # we consider each of [i, i+1].. [i, i+d]
        # and we take each integer, and add it to the set
        # and continue from ahead.

        total = int(n * (n+1) / 2)
        tmp = n
        d = 0
        while tmp > 0:
            d += 1
            tmp = int(tmp / 10)
        
        print(f"total={total}, n={n}, d={d}")
        len_s = len(s)

        zero = ord('0')
        def get_missing(pos: int, seen: Set[int]) -> int:
            # print(f"pos is {pos}, seen is {seen}")
            if pos >= len_s:
                if len(seen) == (n-1):
                    #find the missing number
                    return total - sum(seen)
                else:
                    return 0
            
            # print("here")
            if s[pos] == '0':
                return 0

            num = 0
            for i in range(1, d+1):
                num = num * 10 + (ord(s[pos+i-1]) - zero)
                if num > n or num in seen:
                    break

                seen.add(num)
                res = get_missing(pos + i, seen)
                if res != 0:
                    return res
                seen.remove(num)
            
            return 0

        return get_missing(0, set())

import sys

if __name__ == "__main__":
    s = Solution()
    string = str(sys.argv[1])
    n = int(sys.argv[2])
    # print(f"{string}, {n}")
    print(s.findMissingNumber(string, n))