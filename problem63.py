'''

The number of digits in a^b is [D = 1 + Log10(a^b)](floor function)
Upper bound -> 9^n,

D = 1 + n(Log10(9))


'''

from math import log10

def powerful_digit():
	
	'''
	>>> powerful_digit()
	49
	'''
	
	i = 0

	for num in range(1, 10):

		i += int(1 / (1 - log10(num)))

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
