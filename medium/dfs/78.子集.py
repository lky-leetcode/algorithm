#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, cur, ans, path):
            ans.append(path[:])
            for i in range(cur, len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1, ans, path)
                path.pop()
        ans = []
        dfs(nums, 0, ans, [])
        return ans
# @lc code=end

