import random
class grid:
    def __init__(self, n = 3):
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
        line1 = random.randrange(0, self.n, 1)
        line2 = random.randrange(0, self.n, 1)
        while (line2 == line1):
            line2 = random.randrange(0, self.n, 1)
        box = random.randrange(0, self.n, 1)
        l1 = box*self.n + line1
        l2 = box*self.n + line2
        self.table[l1], self.table[l2] = self.table[l2], self.table[l1]

    def swap_columns(self):
        """Swap the two columns in a line of boxes"""
        grid.transposing(self)
        grid.swap_rows(self)
        grid.transposing(self)  

    def swap_row_boxes(self):
        """Swap the row of boxes"""
        box1 = random.randrange(0, self.n, 1)
        box2 = random.randrange(0, self.n, 1)
        while (box2 == box1):
            box2 = random.randrange(0, self.n, 1)
        for i in range(0, self.n):
            l1, l2 = box1*self.n + i, box2*self.n + i
            self.table[l1], self.table[l2] = self.table[l2], self.table[l1]

    def swap_column_boxes(self):
        """Swao the column of boxes"""
        grid.transposing(self)
        grid.swap_row_boxes(self)
        grid.transposing(self)  

    def mix(self, stp = 10):
        mix_func = ['self.transposing()', 
					'self.swap_rows()', 
					'self.swap_columns()', 
					'self.swap_row_boxes()', 
					'self.swap_column_boxes()']
        for i in range(1, stp):
            id_func = random.randrange(0, len(mix_func), 1)
            eval(mix_func[id_func])

example = grid()
example.mix()

flook = [[0 for j in range(example.n ** 2)] for i in range(example.n ** 2)]
iterator = 0
difficulty =  example.n ** 4

example.show()
print("--------------------------")

while iterator < exmaple.n ** 4
    i, j = random.randrange(0, example.n ** 2, 1), random.randrange(0, example.n ** 2, 1)
    if flook[i][j] == 0:
        iterator += 1
        flook[i][j] = 1

        temp = example.table[i][j] #save the element if something goes wrong
        example.table[i][j] = 0
        difficulty -= 1
        
        table_solution = []
        for solution in solver.