#
# @lc app=leetcode.cn id=99 lang=python
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
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        def find_swap(nums):
            x = y = -1
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x,y
        def traversal_recover(root, x, y):
            if not root:
                return
            if root.val == x:
                root.val = y
            elif root.val == y:
                root.val = x
            traversal_recover(root.left, x, y)
            traversal_recover(root.right, x, y)

        if not root:
            return 
        nums = inorder(root)
        x,y = find_swap(nums)
        traversal_recover(root, x, y)
        return root
# @lc code=end

