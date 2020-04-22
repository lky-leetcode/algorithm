#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.m = float('-inf')
        ans = []
        def dfs(root, l):
            if not root:
                return
            if l > self.m:
                ans.append(root.val)
                self.m = l
            dfs(root.right, l + 1)
            dfs(root.left, l + 1)
        dfs(root, 0)
        return ans
# @lc code=end

