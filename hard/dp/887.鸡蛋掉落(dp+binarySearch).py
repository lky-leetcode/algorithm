#
# @lc app=leetcode.cn id=887 lang=python
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

        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][1] = i
        
        for i in range(1, K + 1):
            dp[1][i] = 1


        for i in range(2, N + 1):
            for j in range(2, K + 1):
                l = 1
                r = i
                while l < r:
                    mid = (l + r)// 2
                    broken = dp[mid - 1][j - 1]
                    nbroken = dp[i - mid][j]
                    if broken > nbroken:
                        r = mid - 1
                    elif broken < nbroken:
                        l = mid + 1
                    else:
                        l = r = mid
                dp[i][j] = min(max(dp[r - 1][j - 1], dp[i - r][j]), max(dp[l - 1][j - 1], dp[i - l][j])) + 1
        return dp[N][K]

# @lc code=end

