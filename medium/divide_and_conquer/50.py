class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        y = self.myPow(x, n // 2)
        if n % 2 == 1:
            return x * y * y
        else:
            return y * y
