def init_sum():
	initial_sum = 0
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			initial_sum += i
		
	'''
	>>> init_sum()
	233168
	'''
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
