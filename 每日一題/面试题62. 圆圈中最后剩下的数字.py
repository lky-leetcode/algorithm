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