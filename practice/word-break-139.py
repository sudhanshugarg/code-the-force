from typing import List, Optional
from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we have a list of words
        # put them all into a Trie
        # lets start with s
        # each time we hit a word, we trigger a search for the remainder of the sentence
        # we also continue with the same sentence as is. if either return true, done.
        # to return true, we should hit a word at teh end of s.
        root = Trie()
        m = len(wordDict)
        for i in range(m):
            root.insert(wordDict[i], 0, len(wordDict[i]))
        
        n = len(s)

        # optimization 1. create a dict that contains all pairs i,j, such that these are either
        # possible or not possible to make. reuse these when possible.
        dp = dict()

        def dfs(index: int, t: Trie, start: int) -> bool:
            if index >= n:
                return False

            substr = (start, index) # inclusive of start and index
            if substr in dp:
                return dp[substr]

            next_tree = t.find(s[index])
            if not next_tree:
                dp[substr] = False
                return False
        
            if next_tree.word_end:
                if index == n-1:
                    dp[substr] = True
                    return True
                # start a recursive search
                dp[substr] = dfs(index+1, next_tree, start) or dfs(index+1, root, index+1)
            else:
                dp[substr] = dfs(index+1, next_tree, start)

            return dp[substr]

        return dfs(0, root, 0)

class Trie:
    def __init__(self):
        self.subtree: List[Optional[Trie]] = [None] * 26
        self.word_end = False

    def insert(self, w: str, index: int, n: int):
        a = ord('a')
        j = ord(w[index]) - a
        if not self.subtree[j]:
            self.subtree[j] = Trie()

        if index < n-1:
            self.subtree[j].insert(w, index+1, n)
        else:
            self.subtree[j].word_end = True

    def find(self, c: chr):
        return self.subtree[ord(c) - ord('a')]

if __name__ == "__main__":
    sol = Solution()
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"]
    s = "aaaaaaaaaaaaaaaaaaaaa"
    print(sol.wordBreak(s, wordDict))