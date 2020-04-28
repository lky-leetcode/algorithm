# 全部xor找到第一個1，做分組，0的1組，1的一組

class Solution:
	def singleNumbers(self, nums):
		x = 0
		for i in nums:
			x ^= i
		start = 0
		while x:
			if not (x & 1):
				start += 1
				x >>= 1
			else:
				break
		a = 0
		b = 0
		for i in nums:
			if (i >> start) & 1:
				a ^= i
			else:
				b ^= i 
		return [a, b]
'''
if __name__ == '__main__':
	sol = Solution()
	nums = [1, 2, 5, 2]
	print (sol.singleNumbers(nums))
'''
