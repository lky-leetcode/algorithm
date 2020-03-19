class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        else :
            return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + root.val