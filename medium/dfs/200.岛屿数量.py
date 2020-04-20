#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]):
        
        def dfs(grid, i, j, group):
            m, n = len(grid), len(grid[0])
            dir = [(1, 0),(0, 1),(-1 , 0),(0, -1)]
            grid[i][j] = group
            for dx, dy in dir:
                if (0 <= i + dx < m) and (0 <= j + dy < n):
                    if grid[i + dx][j + dy] == "1":
                        dfs(grid, i + dx, j + dy, group)
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        group = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j, group)
                    group += 1
        return group - 2
# @lc code=end

