from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        lr_row = 0
        down_col = n-1
        rl_row = m-1
        up_col = 0

        result = []
        direction = 0
        while lr_row < rl_row and up_col < down_col:
            #4 for loops
            #lr_row, up_col to lr_row, down_col-1
            #lr_row, down_col to rl_row-1, down_col
            #rl_row, down_col to rl_row, up_col+1
            #rl_row, up_col to lr_row+1, up_col
            result.extend(matrix[lr_row][up_col:down_col])

            for r in range(lr_row, rl_row):
                result.append(matrix[r][down_col])

            result.extend(matrix[rl_row][down_col:up_col:-1])

            for r in range(rl_row, lr_row, -1):
                result.append(matrix[r][up_col])

            lr_row += 1
            down_col -= 1
            rl_row -= 1
            up_col += 1
        
        
        return result

#test cases
#1 row
#1 col
#2 rows
#3 rows
#4 rows
