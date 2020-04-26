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
        
        def dfs(nums, ans, cur, path, visited):
            ans.append(path[:])
            for i in range(cur, len(nums)):
                if i > 0 and not visited[i - 1] and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(nums, ans, i + 1, path, visited)
                path.pop()
                visited[i] = False
        ans = []
        nums.sort()
        visited = [False] * len(nums)
        dfs(nums, ans, 0, [], visited)
        return ans
# @lc code=end

