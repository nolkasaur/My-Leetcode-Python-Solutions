# https://leetcode.com/problems/valid-sudoku/
# 88 ms, 16.55 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_box = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in sub_box[i // 3, j // 3]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sub_box[i // 3, j // 3].add(board[i][j])
        return True
