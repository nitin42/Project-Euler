'''

Solution: Just see that the number of digits present in the multiple of 6X are present in X.

'''

# while loop iterator

def multiple():
	
	'''
	>>> multiple()
	142857
	'''
	
	i = 1

	while True:
		if set(str(i)) == set(str(6*i)):
			if set(str(i)) == set(str(5*i)):
				if set(str(i)) == set(str(4*i)):
					if set(str(i)) == set(str(3*i)):
						if set(str(i)) == set(str(2*i)):
							print i
							break
		i += 1

if __name__ == '__main__':
	import doctest 
	doctest.testmod(verbose=True)
