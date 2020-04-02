#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        neg = 1
        pos = 1
        flag = 0
        for i in range(len(string)):
            if string[i] == ' ' and ans == 0 and flag == 0:
                continue
            elif ord('0') <= ord(string[i]) <= ord('9'):
                flag = 1
                ans = ans * 10 + ord(string[i]) - 48
            elif string[i] == '-' and ans == 0 and neg == 1 and pos == 1 and flag == 0:
                flag = 1
                neg = -1
            elif string[i] == '+' and ans == 0 and pos == 1 and neg == 1 and flag == 0:
                flag = 1
                pos = 2
            else:
                break
        ans = ans * neg
        if ans > 2147483647:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans
                 
# @lc code=end

