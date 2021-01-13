class grid:
	def __init__(self,n = 3):
        """Generation of the base table"""
        
        self.n = n
		self.table = [[((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]

    def transposing(self):
        """Transponing the whole grid"""
        self.table = map(list, zip(*self.table))

	def __del__(self):
		pass
	
	def show(self):
        """Showing the whole grid"""
		for i in range(self.n*self.n):
			print (self.table[i])
    
    def swap_rows(self):
        """Swap the two rows in a line of boxes"""
        line1 = random.randrange(0,self.n,1)
        line2 = random.randrange(0,self.n,1)
        while (line2 == line1):
            line2 = random.randrange(0,self.n,1)
        box = random.randrange(0,self.n,1)
        l1 = box*self.n + line1
        l2 = box*self.n + line2
        self.table[l1], self.table[l2] = self.table[l2], self.table[l1]
    
    def swap_columns(self):
        """Swap the two columns in a line of boxes"""
        grid.transposing(self)
        grid.swap_rows(self)
        grid.transposing(self)  

    def swap_rboxs(self):
        """Swap the rows of boxes"""
        box1 = random.randrange(0,self.n,1)
        box2 = random.randrange(0,self.n,1)
        while (box2 == box1):
            box2 = random.randrange(0,self.n,1)
        for i in range(0, self.n):
            l1, l2 = box1*self.n + i, box2*self.n + i
            self.table[l1], self.table[l2] = self.table[l2], self.table[l1]

    def swap_cboxes(self):
        """Swao the column of boxes"""
        grid.transposing(self)
        grid.swap_rboxes(self)
        grid.transposing(self)  

    def mix(self,stp = 10):
        mix_func = ['self.transposing()', 
					'self.swap_rows()', 
					'self.swap_columns()', 
					'self.swap_rboxes()', 
					'self.swap_cboxes()']
        for i in xrange(1, stp):
            id_func = random.randrange(0, len(mix_func),1)
            eval(mix_func[id_func])
a = grid(n = 3)
a.show