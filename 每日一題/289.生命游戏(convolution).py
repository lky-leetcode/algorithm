#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start

class Solution(object):
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        r, c=len(board), len(board[0])
        #zero padding
        board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
        board_exp[1 : 1 + r, 1 : 1 + c] = np.array(board)
        #卷積參數
        kernel = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]])
        #卷積
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                #統計八個位置
                temp_sum = np.sum(kernel * board_exp[i - 1 : i + 2, j - 1 : j + 2])
                if board_exp[i, j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i - 1][j - 1] = 0
                else:
                    if temp_sum == 3:
                        board[i - 1][j - 1] = 1
        return board          

        
# @lc code=end

