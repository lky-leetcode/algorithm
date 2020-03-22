#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isMirror(t1, t2):
            if not (t1 or t2):
                return True
            if not (t1 and t2):
                return False
            return (t1.val == t2.val) and \
                    isMirror(t1.right, t2.left) and \
                    isMirror(t1.left, t2.right)
        return isMirror(root.left, root.right)
# @lc code=end

