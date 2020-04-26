#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.visited = [False] * len(nums)
        def dfs(nums, ans, path, visited):
            if len(nums) == len(path):
                ans.append(path[:])
                #print(f"ans = {ans}")
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                path.append(nums[i])
                #print(f"path = {path}")
                dfs(nums, ans, path, visited)
                path.pop()
                visited[i] =False


        ans = []
        path = []
        nums.sort()
        dfs(nums, ans, path, self.visited)
        return ans
# @lc code=end

