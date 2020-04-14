#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l = ListNode()
        h = l
        while l1 or l2:
            if l1 and not l2:
                l.val = (carry + l1.val) % 10
                carry = (carry + l1.val) // 10
                l1 = l1.next
            elif l2 and not l1:
                l.val = (carry + l2.val) % 10
                carry = (carry + l2.val) // 10
                l2 = l2.next
            else:
                l.val = (carry + l1.val + l2.val) % 10
                carry = (carry + l1.val + l2.val) // 10
                l1 = l1.next
                l2 = l2.next
            if l1 or l2 or carry:
                newNode = ListNode()
                l.next = newNode
                l = l.next
            if not l1 and not l2 and carry:
                l.val = carry
        return h
# @lc code=end

