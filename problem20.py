def factorial(num):
	fact = 1

	# check if the number is negative, positive or zero
	if num < 0:
		return num
	else:
		for i in range(1,num + 1):
			fact = fact*i
		#print(factorial)

	a = (list(str(fact)))
   	
   	b = map(int, a)

   	c = sum(b)

   	print c

   	'''
   	>>> factorial(2)
   	4
   	'''


if __name__ == '__main__':
	import doctest
	doctest.testmod()
