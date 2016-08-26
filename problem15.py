from math import factorial

def grid_binomial():
	'''
	>>> grid_binomial()
	815915283247897734345611269596115894272000000000
	'''
	
	n = 20
	m = 20

	combinate = factorial(n + m)// factorial(n) * factorial(m)

	print combinate

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)