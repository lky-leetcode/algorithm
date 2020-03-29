#
# @lc app=leetcode.cn id=687 lang=python3
# 
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.Max = 0
        def traversalMax(root):
            if not root:
                return 0
            left = traversalMax(root.left)
            right = traversalMax(root.right)
            if root.left and root.left.val == root.val:
                left = left + 1
            else :
                left = 0
            if root.right and root.right.val == root.val:
                right = right + 1
            else :
                right = 0
            self.Max =  max(self.Max, left + right)
            return max(left, right)
            
        traversalMax(root)
        return self.Max
# @lc code=end

