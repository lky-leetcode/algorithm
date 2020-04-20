#
# @lc app=leetcode.cn id=1025 lang=python
#
# [1025] 除数博弈
#

# @lc code=start
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        self.ans = 0
        def dfs(user, n):
            if n == 0 or n == 1:
                return user
            for i in range(1, n):
                if (n % i) == 0 and (n - i) >= 0:
                    nums = dfs(user + 1, n - i)
                    if nums % 2 == 1:
                        self.ans = 1
                    return nums
        dfs(0, N)
        return self.ans
# @lc code=end

