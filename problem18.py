'''
Requires concept of dynamic programming. A bottom up dynamic programming solution is to 
allocate a number triangle that stores the maximum reachable sum if we were to start from 
that position. It is easy to compute the number triangle from the bottom row onward using 
the fact that the
				best from this point = this point + max(best from left, best from right)

What we can do is that store the path or graph in a text file, form an 2-D array of that graph
and iterate using the above concept.
'''

def max_path():
	'''
	>>> max_path()
	1074
	'''

	arr = [map(int, i.split()) for i in open('list.txt').readlines()]

	for row in range(len(arr)-1, 0, -1):
		for col in range(0, row):
			arr[row-1][col] += max(arr[row][col], arr[row][col+1])

	print arr[0][0]

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)