class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for num in nums:
            total += num
        
        return int(n * (n+1) / 2) - total