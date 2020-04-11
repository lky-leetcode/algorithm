#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        
        if K == 1:
            return N
        if N == 1:
            return 1 
        
        minTemp = float('inf')
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][1] = i
        
        for i in range(1, K + 1):
            dp[1][i] = 1


        for i in range(2, N + 1):
            for j in range(2, K + 1):
                minTemp = float('inf')
                for s in range(1, i + 1):
                    maxTemp = max(dp[s - 1][j - 1], dp[i - s][j]) + 1
                    minTemp = maxTemp if minTemp > maxTemp else minTemp
                dp[i][j] = minTemp


        return dp[N][K]

# @lc code=end

