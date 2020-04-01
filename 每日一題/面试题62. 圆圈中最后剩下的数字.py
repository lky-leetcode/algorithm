'''

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

'''

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = [i for i in range(n)]
        cur = 0
        if n == 0 or m == 0:
            return -1
        while len(l) != 1:
            pop_num = (cur + m - 1) % len(l)
            l.pop(pop_num)
            cur = pop_num 
        return l[0] 
