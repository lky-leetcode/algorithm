'''
给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。

24nd two weekly contest
第1題
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        for i in range(1, 5051):
            s = i
            for j, value in enumerate(nums):
                s += value
                if s < 1:
                    break
                if j == len(nums) - 1 and s >= 1:
                    return i
        return i