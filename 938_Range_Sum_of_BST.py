# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.traversal(root, L, R)

    def traversal(self, root, L, R):
        if not root:
            return 0
        if L <= root.val <= R:
            self.ans += root.val
            self.traversal(root.right, L, R)
            self.traversal(root.left, L, R)
        if root.val < L:
            self.traversal(root.right, L, R)
        if root.val > R:
            self.traversal(root.left, L, R)
        return self.ans