'''
1. Calculate the reverse of a number and it to the number 
itself.

2. If the resultig sum is palindrome then the number is not
lychrel number.

3. So we just calculate the sum and check how many such numbers
are there under ten-thousand.

'''

def is_palindrome(str1):
	if str1 == str1[::-1]:
		return True
	else:
		return False

def lychrel_number():
	s = 0
	count = 0
	for i in range(1, 10000):
		j = str(i)
		a = j + j[::-1]
		if is_palindrome(a):
			count += 1

	print count

	'''
	>>>9999
	'''


if __name__ == '__main__':
	import doctest
	doctest.testmod()
