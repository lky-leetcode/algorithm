#Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
#Return how many groups have the largest size.
#23nd two weekly contest
#第1題

class Solution:
    def countLargestGroup(self, n: int) -> int:
        nums = [0] * 100
        maxbit = 0
        ans = 0
        def count(number):
            result = 0
            while number != 0:
                result += number % 10
                number //= 10
            return result

        for i in range(1, n + 1):
            bit = count(i)
            nums[bit] += 1
            maxbit = max(nums[bit], maxbit)
            
        for i in range(1, 100):
            if nums[i] == maxbit:
                ans += 1
        return ans
            