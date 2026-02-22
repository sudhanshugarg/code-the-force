class Solution:
    def twoSum(self, arr: List[int], t: int) -> List[int]:
        # two pointer approach
        # l and r
        # find the first set of l and r that sum to t.
        # there will always be exactly 1 solution.

        n = len(arr)
        l = 0
        r = n-1
        while l < r:
            sum = arr[l] + arr[r]
            if sum < t:
                l += 1
            elif sum > t:
                r -= 1
            else:
                return [l+1, r+1]
        
        return []