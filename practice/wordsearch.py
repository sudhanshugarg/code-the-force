from typing import Dict, List

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        # just do dfs from every cell, if any of them return true. done.
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        freq_board = {}
        freq_word = {}
        for i in range(26):
            freq_board[chr(ord('a') + i)] = 0
            freq_board[chr(ord('A') + i)] = 0
            freq_word[chr(ord('a') + i)] = 0
            freq_word[chr(ord('A') + i)] = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                freq_board[board[i][j]] += 1        

        for i in range(len(word)):
            freq_word[word[i]] += 1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs_find_freq(board, i, j, 0, word, m, n, visited, freq_board, freq_word, 0):
                    return True
        return False

    def dfs_find(self, board: List[List[str]], r: int, c: int, word_index: int, word: str, m: int, n: int, visited: List[List[bool]]) -> bool:
        if board[r][c] != word[word_index]:
            return False
        elif word_index == len(word) - 1:
            return True

        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        visited[r][c] = True
        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                continue

            if self.dfs_find(board, nr, nc, word_index + 1, word, m, n, visited):
                return True
        visited[r][c] = False
        return False

    def dfs_find_freq(self, board: List[List[str]], r: int, c: int, word_index: int, word: str, m: int, n: int, visited: List[List[bool]],
                      freq_board: Dict[str, int], freq_word: Dict[str, int], visited_letter_count: int) -> bool:
        if board[r][c] != word[word_index]:
            return False
        elif word_index == len(word) - 1:
            return True


        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        visited[r][c] = True
        visited_letter_count += 1
        letter_index = board[r][c]
        freq_board[letter_index] -= 1
        freq_word[letter_index] -= 1
        if self.not_enough_correct_letters_left(freq_board, freq_word) or self.not_enough_board_letters_left(len(word) - word_index - 1, m*n - visited_letter_count):
            return False

        for i in range(4):
            nr = r + dirs[i][0]
            nc = c + dirs[i][1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                continue

            if self.dfs_find_freq(board, nr, nc, word_index + 1, word, m, n, visited, freq_board, freq_word, visited_letter_count):
                return True
        visited[r][c] = False
        freq_board[letter_index] += 1
        freq_word[letter_index] += 1
        visited_letter_count -= 1
        return False
    
    def not_enough_board_letters_left(self, word_letters_left: int, board_letters_left: int) -> bool:
        return word_letters_left > board_letters_left
    
    def not_enough_correct_letters_left(self, board_letters_left_freq: Dict[str, int], word_letters_left_freq: Dict[str, int]) -> bool:
        for key, value in board_letters_left_freq.items():
            if value < word_letters_left_freq[key]:
                return True
        return False