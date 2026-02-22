from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #define helper, that returns list from index i onwards
        #add current number at each position in that list.
        #return all these lists
        n = len(nums)

        return self.permuteHelper(0, n, nums)
    
    def permuteHelper(self, index: int, n: int, nums: List[int]) -> List[List[int]]:
        if index >= n:
            return []
        elif index == n-1:
            return [[nums[index]]]
        
        permutations = self.permuteHelper(index+1, n, nums)
        result = []
        list_len = n - index
        for p in permutations:
            for i in range(list_len):
                next_list = []
                next_list.extend(p[:i])
                next_list.append(nums[index])
                next_list.extend(p[i:])
                result.append(next_list)
        
        return result