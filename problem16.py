def power(num):
	'''
	>>> power(1000)
	1366
	'''
	a = 2**num
	b = list(str(a))
	res = [int(i) for i in b]
	print sum(res)

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
