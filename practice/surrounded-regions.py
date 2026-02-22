from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        start from each edge, do dfs and mark each O node as V
        once all done, then go through entire board and mark all remaining
        O's as X, and all V's as O

        for the dfs, dont need to reset it, just keep going.
        """
        m = len(board)
        n = len(board[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = 'V'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)    
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'