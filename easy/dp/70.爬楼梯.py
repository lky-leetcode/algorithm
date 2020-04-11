#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 , 1, 2]
        for i in range(3 ,n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]
# @lc code=end

