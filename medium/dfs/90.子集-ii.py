#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(nums, ans, cur, path):
            ans.append(path[:])
            for i in range(cur, len(nums)):
                if i > cur and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(nums, ans, i + 1, path)
                path.pop()
        ans = []
        nums.sort()
        dfs(nums, ans, 0, [])
        return ans
# @lc code=end

