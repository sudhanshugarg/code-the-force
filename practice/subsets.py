from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        recursive
        choose element i, add it into all subsets from i+1
        don't choose element i, get all subsets without it
        at each step, keep choosing to add element or not
        at the root, add these elements to the ans
        """

        powerset = []
        n = len(nums)
        def dfs(index: int, curr_list: List[int]):
            if index >= n:
                powerset.append(curr_list.copy())
                return

            # add nums[index]
            curr_list.append(nums[index])
            dfs(index + 1, curr_list)
            curr_list.pop()
            # do not add nums[index]
            dfs(index+1, curr_list)            

        dfs(0, [])
        return powerset
        