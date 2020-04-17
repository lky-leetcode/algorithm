#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxLeft = 0
        for i, value in enumerate(nums):
            if maxLeft >= len(nums) - 1:
                return True
            if i <= maxLeft:
                maxLeft = max(maxLeft, i + value)
            else:
                return False


# @lc code=end

