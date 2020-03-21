#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, low = float('-inf'), high = float('inf')):
        if not root:
            return True
        if not low < root.val < high:
            return False
        return self.isValidBST(root.left,low,root.val) and \
               self.isValidBST(root.right,root.val,high)


# @lc code=end

