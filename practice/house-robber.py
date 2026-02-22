class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [[0, 0] for _ in range(n)]
        arr[0][1] = nums[0]

        for i in range(1, n):
            arr[i][0] = max(arr[i-1][0], arr[i-1][1])
            arr[i][1] = nums[i] + arr[i-1][0]
        
        return max(arr[n-1][0], arr[n-1][1])