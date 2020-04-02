#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #define 1->0 3
        #define 0->1 4
        self.countAlive = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.countAlive = 0
                if (board[i][j] == 1):
                    if (i > 0  and j > 0 and board[i - 1][j - 1] % 2):
                        self.countAlive += 1
                    if (i > 0 and board[i - 1][j] % 2):
                        self.countAlive += 1
                    if (i > 0 and j + 1 < len(board[i]) and board[i - 1][j + 1] % 2):
                        self.countAlive += 1
                    if (j > 0 and board[i][j - 1] % 2):
                        self.countAlive += 1
                    if (j + 1 < len(board[i]) and board[i][j + 1] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and j > 0 and board[i + 1][j - 1] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and board[i + 1][j] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and j + 1 < len(board[i]) and board[i + 1][j + 1] % 2):
                        self.countAlive += 1
                    if self.countAlive > 3 or self.countAlive < 2:
                        board[i][j] = 3
                else :
                    if (i > 0  and j > 0 and board[i - 1][j - 1] % 2):
                        self.countAlive += 1
                    if (i > 0 and board[i - 1][j] % 2):
                        self.countAlive += 1
                    if (i > 0 and j + 1 < len(board[i]) and board[i - 1][j + 1] % 2):
                        self.countAlive += 1
                    if (j > 0 and board[i][j - 1] % 2):
                        self.countAlive += 1
                    if (j + 1 < len(board[i]) and board[i][j + 1] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and j > 0 and board[i + 1][j - 1] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and board[i + 1][j] % 2):
                        self.countAlive += 1
                    if (i + 1 < len(board) and j + 1 < len(board[i]) and board[i + 1][j + 1] % 2):
                        self.countAlive += 1
                    if self.countAlive == 3:
                        board[i][j] = 4

        print(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                #print(board[i][j])
                if (board[i][j] == 3):
                    board[i][j] = 0
                elif(board[i][j] == 4):       
                    board[i][j] = 1
        
# @lc code=end

