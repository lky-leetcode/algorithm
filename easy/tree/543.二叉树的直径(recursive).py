#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        def traversal(root):
            if not root:
                return 
            cur = maxDepth(root.left) + maxDepth(root.right)
            if (cur > self.max):
                self.max = cur
            traversal(root.left)
            traversal(root.right)

        def maxDepth(root):
            if not root:
                return 0
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        traversal(root)
        return self.max


# @lc code=end

