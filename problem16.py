def power(num):
	a = 2**num
	b = list(str(a))
	res = [int(i) for i in b]
	print sum(res)

	'''
	>>> power(1000)
	1366
	'''

if __name__ == '__main__':
	import doctest
	doctest.testmod()
