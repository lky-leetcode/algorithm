#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def traversal_recover(root):
            nonlocal x, y, prev
            if not root:
                return
            traversal_recover(root.left)
            if prev and root.val < prev.val:
                y = root
                if not x:
                    x = prev
                else :
                    return
            prev = root
            traversal_recover(root.right)

        if not root:
            return
        x = y = prev = None
        traversal_recover(root)
        x.val, y.val = y.val, x.val
# @lc code=end

