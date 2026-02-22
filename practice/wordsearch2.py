from typing import List, Optional, Set

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        def insert(trie: TrieNode, word: str, index: int):
            first_letter_index = ord(word[index]) - ord('a')
            curr_trie = trie.nodes[first_letter_index]

            if curr_trie is None:
                curr_trie = trie.nodes[first_letter_index] = TrieNode(first_letter_index)
            
            if index == len(word) - 1:
                curr_trie.is_word = True
                curr_trie.word = word
                return
            else:
                insert(curr_trie, word, index + 1)

        result = set()

        def get_existing(root: Optional[TrieNode], r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == "#":
                return

            if root is None:
                return

            letter = board[r][c]
            #print(letter)
            letter_index = ord(letter) - ord('a')
            next_root = root.nodes[letter_index]
            if next_root is None:
                return

            board[r][c] = '#'
            if next_root.is_word:
                result.add(next_root.word)

            get_existing(next_root, r+1, c)
            get_existing(next_root, r-1, c)
            get_existing(next_root, r, c+1)
            get_existing(next_root, r, c-1)
            board[r][c] = letter
            return
            

        root = TrieNode(-1)
        for word in words:
            insert(root, word, 0)

        
        for i in range(m):
            for j in range(n):
                get_existing(root, i, j)
        
        return [word for word in result]

"""
ans1: brute force: find each word, and if found, add to the result list. to find a single word, use earlier method.
ans2: inverse the board and the word search. basically build a prefix trie from the words, and then use the board to check if any word exists. if it does, add it to the result set.
"""

class TrieNode:
    def __init__(self, id: int):
        self.nodes: List[Optional[TrieNode]] = [None for _ in range(26)]
        self.val = id
        self.is_word = False
        self.word = ""
