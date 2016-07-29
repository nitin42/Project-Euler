def prime(n):
	l = []
	for num in range(2, n+1):
		if num>1:
			for i in range(2, num):
				if num%i == 0:
					break
			else:
				l.append(num)
	print sum(l)
	
if __name__ == '__main__':
	prime(2000000)