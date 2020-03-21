#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans=[]
        if not root:
            return root
        def postTraversal(node):
            if not node:
                return 
            for cur in node.children:
                postTraversal(cur)
            ans.append(node.val)
        postTraversal(root)
        return ans
# @lc code=end

