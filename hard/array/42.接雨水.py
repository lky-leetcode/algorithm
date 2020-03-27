#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 邊界條件
        if not height: 
            return 0
        # init
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        maxleft[0] = height[0]
        maxright[n - 1] = height[n - 1]
        
        for i in range(1, n):
            maxleft[i] = max(height[i], maxleft[i - 1])
        for j in range(n - 2, -1, -1):
            maxright[j] = max(height[j],maxright[j + 1])
    
        for i in range(n):
            if min(maxleft[i], maxright[i]) > height[i]:
                ans += min(maxleft[i], maxright[i]) - height[i]
        return ans

# @lc code=end

