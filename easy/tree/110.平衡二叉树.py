#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traversal(root):
            if not root:
                return True
            maxL = maxDepth(root.left) if root.left else 0
            maxR = maxDepth(root.right) if root.right else 0
            if abs(maxL - maxR) > 1:
                return False
            return traversal(root.left) and traversal(root.right)
            
        def maxDepth(root):
            if not root:
                return 0
            return max(maxDepth(root.right), maxDepth(root.left)) + 1

        if not root:
            return True
        return traversal(root)
# @lc code=end

