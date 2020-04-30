class Solution:
	def isHappy(self, n: int) -> bool:
		visited = set()
		def getNext(n):
			sum = 0
			while(n):
				digit = n % 10
				n //= 10
				sum += digit*digit
			return sum
		visited.add(n)
		while(n != 1):
			n = getNext(n)
			if n in visited:
				return False
			else:
				visited.add(n)
		return True
