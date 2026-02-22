from typing import List

class Solution:
    def findMin(self, nums: List[int]):
        n = len(nums)

        def binsearch(low: int, high: int):
            while low < high:
                if nums[low] < nums[high]:
                    break
         
                mid = int((low + high) / 2)
                #one array is low to mid, other is mid+1 to high
                if nums[low] > nums[mid]:
                    high = mid
                elif nums[mid+1] > nums[high]:
                    low = mid+1
                else:
                    low = mid+1
                    break

            return nums[low]

        return binsearch(0, n-1)

#test cases
#4 5 6 7 8 1 2 3
# low, high, mid = 0, 7, 3
# 4, 7, 5
# 4, 5, 4
# 4, 4, 4
# yes

# #6 7 8 1 2 3 4
# 0, 6, 3
# 0, 3, 1
# 2, 3, 2
# 2, 2, 2
# yes


# #6 7 1 2 3 4
# 0, 5, 2
# 0, 2, 1
# yes


# #1 2 3 4
# yes

# #7 1 6
# 0, 2, 1
# 0, 1, 0

