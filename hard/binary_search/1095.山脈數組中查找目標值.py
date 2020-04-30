# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class Solution:
	def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
		l, r = 0, mountain_arr.length()
		while l > r :
			m = l + (r - l ) // 2
			if f(m): 
				return
			if g(m):
				r = m
			else:
				l = m + 1
		
