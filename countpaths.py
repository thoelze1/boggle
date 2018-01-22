from numpy import matrix
m = 6
n = 6
graph = []
for k in range(m * n):
	row = m * n * [0]
	# Horizontal gridlines
	if ((k + 1) % n) != 0:
		row[k+1] = 1
	if (k % n) != 0:
		row[k-1] = 1
	# Vertical gridlines
	if (k + n) < (m * n):
		row[k+n] = 1
	if (k - n) >= 0:
		row[k-n] = 1
	# \ diagonals
	if (k % n) != (n - 1) and k < ((m-1) * n):
		row[k+n+1] = 1
	if (k % n) != 0 and k >= n:
		row[k-n-1] = 1
	# / diagonals
	if (k % n) != (n - 1) and k >= n:
		row[k-n+1] = 1
	if (k % n) != 0 and k < (m-1) * n:
		row[k+n-1] = 1
	graph.append(row)
numPaths = 0
A = matrix(graph)
for i in range(1, m * n):
	power = A**i
	print("Paths of length " + str(i) + ": " + str(power.sum()))
	numPaths += power.sum()
print("Total paths: " + str(numPaths))
