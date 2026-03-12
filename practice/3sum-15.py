from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        d = defaultdict(lambda: [])

        for i in range(n):
            d[nums[i]].append(i) #d each value is sorted
        
        result = []
        zeros = False
        for i in range(n):
            for j in range(i+1, n):
                sum2 = nums[i] + nums[j]
                if -sum2 in d:
                    indexes = d[-sum2]
                    n2 = len(indexes)
                    for k in range(n2-1, -1, -1):
                        if indexes[k] > j:
                            result.append([i, j, indexes[k]])
                        else:
                            break

        return result