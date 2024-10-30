# https://leetcode.com/problems/word-search/
# 2949 ms, 16.70 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr_rows, nr_cols = len(board), len(board[0])
        def dfs(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= nr_rows or col >= nr_cols or
                word[index] != board[row][col]):
                return False
            board[row][col] = "#"
            continue_next = (dfs(row + 1, col, index + 1) or
                             dfs(row - 1, col, index + 1) or
                             dfs(row, col + 1, index + 1) or
                             dfs(row, col - 1, index + 1))
            board[row][col] = word[index]
            return continue_next
        for r in range(nr_rows):
            for c in range(nr_cols):
                print("yo")
                if dfs(r, c, 0):
                    return True
        return False
