'''
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。

24nd two weekly contest
第2題
'''
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def F(n):
            result_list = []
            a, b = 0, 1
            while n > 0:
                result_list.append(b)
                a, b = b, a + b
                n -= 1
            return result_list
        F_list = F(50)
        count = 0
        for i in range(49, -1 , -1):
            print (F_list[i])
            while k >= F_list[i]:
                k -= F_list[i]
                count += 1
        return count