#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap.get(diff), i]
            hashmap[value] = i
            
# @lc code=end

