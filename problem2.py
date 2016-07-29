def fibo(n):
	a,b = 1,0
	initial_sum = 0
	while n:
		a, b = a+b, a 
			if a%2 == 0:
				initial_sum += a

print initial_sum

if __name__ == '__main__':
	fibo(4000000)