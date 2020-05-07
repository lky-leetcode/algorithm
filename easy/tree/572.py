class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSubtree(self, s, t):
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        if not s and not t:
            return True
        if not s:
            return False
        if isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
