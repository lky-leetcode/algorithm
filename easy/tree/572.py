class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    is_find = True
    ans = False
    def isSubtree(self, s, t):
        def isSameTree(s, t):
            if not s and not t:
                return
            if not s or not t:
                self.is_find = False
                return
            if s.val != t.val:
                self.is_find = False
                return
            isSameTree(s.left, t.left)
            isSameTree(s.right, t.right)
        def traversal(s, t):
            if not s:
                return
            if s.val == t.val:
                self.is_find = True
                isSameTree(s, t)
                if self.is_find == True:
                    self.ans = True
                    return 
            traversal(s.left, t)
            traversal(s.right, t)
        traversal(s, t)
        return self.ans
