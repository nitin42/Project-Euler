def factorial(n):
	f = 1
	if n < 0:
		return False
	else:
		for i in range(1, n+1):
			f = f * i
		return f


def curious_number():
	s = 0
	r = 0
	'''
	upper bound is on 9!*7 = 2540160 which is a seven digit number

	'''
	for i in range(10, 2540161):
		n = i
		while(n>0):
			d = n%10
			n /= 10
			s += factorial(d)

		if (s == i):
			r += i

	print r

if __name__ == '__main__':
	curious_number()