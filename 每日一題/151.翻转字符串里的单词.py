#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #print(s.split())
        l = s.split()
        new_str = ""
        for i in range(len(l) - 1, -1, -1):
            new_str += l[i]
            if i != 0:
                new_str +=" "
        return new_str
# @lc code=end

