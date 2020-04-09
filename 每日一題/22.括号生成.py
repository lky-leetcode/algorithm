#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right, path, ans):
            if left == 0 and right == 0:
                print (path)
                ans.append(path)
            if left > 0 :
                dfs(left - 1, right, path + "(", ans)
            if right > left :
                dfs(left, right - 1, path + ")", ans)
        left = right = n
        ans = []
        path = ""
        dfs(left, right, path, ans)
        return ans 
# @lc code=end

