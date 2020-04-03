#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        cur = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[cur] = nums[i] 
                cur += 1
        return cur
            
# @lc code=end

