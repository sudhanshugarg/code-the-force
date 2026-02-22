from typing import List

class Solution:
    def mergeTriplets(self, trips: List[List[int]], target: List[int]) -> bool:
        """
        first remove all triplets whose any value is greater than target triplet.
        of the remaining triplets, see if each of the targets are covered.

        """
        n = len(trips)
        covered = [False for _ in range(3)]
        for i in range(n):
            if trips[i][0] > target[0] or trips[i][1] > target[1] or trips[i][2] > target[2]:
                continue

            for j in range(3):
                if trips[i][j] == target[j]:
                    covered[j] = True

        return covered[0] and covered[1] and covered[2]
