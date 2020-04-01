#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        a = b = 0  #初始深度都是0
        for s in seq:
            if s == '(':
                if a <= b:
                    a += 1
                    ans.append(0)
                else:
                    b += 1
                    ans.append(1)
            elif s == ')':
                if a > b:
                    a -= 1
                    ans.append(0)
                else:
                    b -= 1
                    ans.append(1)
        return ans
        
# @lc code=end

