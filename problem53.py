from math import factorial

def combinatoric_selection():
	limit = 1000000 # Upto one million
	count = 0
	range_n = 100 # Range of the number
	for i in range(1, 100):
		for j in range(1, i):
			if(factorial(i)/factorial(j)*factorial(i-j) >= limit): # If it exceeds one-million
				count += 1

	print count

	'''
	>>>4589
	'''

if __name__ == '__main__':
	import doctest
	doctest.testmod()


	