#
# @lc app=leetcode.cn id=543 lang=python3
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
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            self.max = max(self.max, l + r)
            return 1 + max(l, r)    
        
        helper(root)
        return self.max


# @lc code=end

