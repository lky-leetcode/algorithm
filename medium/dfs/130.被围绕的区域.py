#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])
        
        def dfs(board, i, j, m, n):
            dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            board[i][j] = 'T'
            for dx, dy in dir:
                if 0 <= i + dx < m and 0 <= j + dy < n:
                    if board[i + dx][j + dy] == 'O':
                        dfs(board, i + dx, j + dy, m, n)

        for i in range(m):
            if (board[i][0] == 'O'):
                dfs(board, i, 0, m, n)
            if (board[i][n-1] == 'O'):
                dfs(board, i, n-1, m, n)
        for j in range(n):
            if (board[0][j] == 'O'):
                dfs(board, 0, j, m, n)
            if (board[m-1][j] == 'O'):
                dfs(board, m-1, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


# @lc code=end

