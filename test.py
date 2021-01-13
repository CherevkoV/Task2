test  =  [[1, 2], [3, 4]]
print(test)
print(zip(*test))
print(map(list, zip(*test)))
n = 3
s = [[((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]
print(s)