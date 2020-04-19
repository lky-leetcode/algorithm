'''
一个 「开心字符串」定义为：

仅包含小写字母 ['a', 'b', 'c'].
对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。

给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。

24nd two weekly contest
第3題
'''
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        c = ['a', 'b', 'c']
        def dfs(happy_string, s, l):
            if l == n:
                happy_string.append(deepcopy(s))
                return
            for i in c:
                if l == 0:
                    s += i
                    dfs(happy_string, s, 1)
                    s = s[:-1]
                elif s[l - 1] != i:
                    s += i
                    dfs(happy_string, s, l + 1)
                    s = s[:-1]
        s = ""
        happy_string = []
        dfs(happy_string, s, 0)
        print (happy_string)
        if k <= len(happy_string):
            return happy_string[k - 1]
        else:
            return ""