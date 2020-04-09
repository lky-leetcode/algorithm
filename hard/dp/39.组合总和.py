#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.combination = []
        if not candidates:
            return []

        def dfs(candidates, remaining, combination, startIndex):
            if remaining == 0:
                self.ans.append(combination[:])
                return
            for i in range(startIndex, len(candidates)): 
                if remaining < candidates[i]:
                    break
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue 
                combination.append(candidates[i])
                dfs(candidates, remaining - candidates[i], combination, i)
                combination.pop()
        candidates.sort()
        dfs(candidates, target, self.combination, 0)
        return self.ans
# @lc code=end

