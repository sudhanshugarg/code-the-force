from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # run twice.
        # start from position 1 and 2. or (i and i+1)
        # compute max at the end
        # for 1, we are leaving out 0, so max at n-1
        # for 2, we are leaving out 1, so max at 0
        if n < 4:
            max_robbery = 0
            for i in range(n):
                max_robbery = max(max_robbery, nums[i])
            return max_robbery


        def compute_max_robbery(s: int) -> int:
            profit = [[0, 0] for _ in range(n)]
            profit[s][1] = nums[s]
            
            prev = s
            curr = 0
            for _ in range(1, n-1):
                curr = (prev + 1) % n
                profit[curr][1] = nums[curr] + profit[prev][0]
                profit[curr][0] = max(profit[prev][0], profit[prev][1])
                prev = curr
            return max(profit[curr][0], profit[curr][1])

        a = compute_max_robbery(1)
        b = compute_max_robbery(2)
        return max(a, b)
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    print(s.rob(nums))