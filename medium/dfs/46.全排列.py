#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, ans, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in nums:
                if i in path:
                    continue
                path.append(i)
                dfs(nums, ans, path)
                path.pop()
                
        ans = []
        path = []
        dfs(nums, ans, path)
        return ans
# @lc code=end

