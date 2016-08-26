def coin_sum(d, k, n):
	'''
	d -> number of denominations(a.k.a coins)
	k -> total numer of ways
	n -> target
	'''

	'''
	>>> d = [1,2,5,10,20,50,100,200]
	>>> k = [1] + [0]*200
	>>> n = 200
	>>> coin_sum(d,k,n)
	73682
	'''

	for coin in d:
		for change in range(coin, n+1):
			k[change] += k[change - coin]

	print k[n] # Print the total number of k ways


if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)