class grid:
	def __init__(self,n = 3):
		self.n = n
		self.table = [[((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]

	def __del__(self):
		pass
	
	def show(self):
		for i in range(self.n*self.n):
			print (self.table[i])