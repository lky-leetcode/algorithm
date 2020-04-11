#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
# @author lky

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l =[] #list for ans
        if not root:
            return []
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        return l    
        
# @lc code=end

