def fibo(n):
	a, b = 1, 0
	count = 0
	while a<n:
		a, b = a+b, a
		count += 1
	return count+1

if __name__ == '__main__':
	print fibo(int('1%s'%('0'*999))) # Because at this number we see our first 1000 digit fibonacci number in series