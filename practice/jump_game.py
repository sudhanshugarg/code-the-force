from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        #canReach = [False] * (n-1)
        closestPossible = n-1

        for i in range(n-2, -1, -1):
            if (closestPossible - i) <= nums[i]:
                #canReach[i] = True
                closestPossible = i
        
        return closestPossible == 0