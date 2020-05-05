# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.ans = True
        self.prev = float('-inf')
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev >= root.val:
                self.ans = False
            self.prev = root.val
            inorder(root.right)

        inorder(root)
        return self.ans
